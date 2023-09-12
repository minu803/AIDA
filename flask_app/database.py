
import sqlite3
import PyPDF2
import numpy as np
import config
from io import BytesIO
import PyPDF2

def create_database():
    # Create the "files" table if it doesn't exist
    with sqlite3.connect(config.database_path) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS files
                        (name TEXT PRIMARY KEY,
                        data BLOB)''')
        conn.commit()

def load_existing_files():
    existing_files = set()
    with sqlite3.connect(config.database_path) as conn:
        c = conn.cursor()
        c.execute('SELECT name FROM files')
        rows = c.fetchall()
        for row in rows:
            existing_files.add(row[0])
    return existing_files

def download_pdfs():
    pdf_names = []

    # Create the directory if it doesn't exist
    if not os.path.exists(config.pdf_path):
        os.makedirs(config.pdf_path)

    existing_files = load_existing_files(config.database_path)

    drive_files = os.listdir(pdf_path)

    with sqlite3.connect(config.database_path) as conn:
        c = conn.cursor()

        for file_name in drive_files:
            if file_name.endswith('.pdf') and file_name not in existing_files:
                pdf_names.append(file_name)
                file_path = os.path.join(pdf_path, file_name)

                # Read the PDF file
                with open(file_path, 'rb') as f:
                    pdf_data = f.read()

                try:
                    # Insert PDF into database
                    c.execute('INSERT INTO files VALUES (?, ?)', (file_name, pdf_data))
                except sqlite3.IntegrityError:
                    # If the file already exists, skip the insertion
                    print(f"File '{file_name}' already exists in the database. Skipping insertion.")

        conn.commit()

def get_book_text(book_name):
    try:
        # Retrieve the book from the database
        with sqlite3.connect(config.database_path) as conn:
            c = conn.cursor()
            c.execute('SELECT data FROM files WHERE name = ?', (book_name,))
            result = c.fetchone()
            if result:
                pdf_data = result[0]
                pdf_file = BytesIO(pdf_data)
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                return text
            else:
                return "No text found for the selected book."
    except Exception as e:
        return str(e)


# import necessary packages
import speech_recognition as sr # https://pypi.org/project/SpeechRecognition/
import queue
from flask import Flask, render_template, Response, request, redirect, url_for, session, jsonify
import time
import threading
import sys
import openai
import config
import sqlite3
import json
import secrets

# import our custom modules
from recorder import *
from transcriber import *
from question_generator import *
from database import *
from age_guidance import *

app = Flask(__name__)
app.debug = True

####################

# Global variable
openai.api_key = config.api_key
app.secret_key = secrets.token_urlsafe(16) # prints a 16 character long url safe secret key

####################

threading.Thread(target=print_result_loop).start()# print output thread
threading.Thread(target=transcribe_loop).start()   # transcribe thread
threading.Thread(target=generate_loop).start()   # transcribe thread


# set up microphone
mic, recorder = init_recording()

@app.route('/')
def index():
    if config.selected_book == '':
        # No book has been selected yet, so redirect to the book selection page
        return redirect(url_for('select_book'))
    else:
        # Continue with your main page's functionality
        # For example, you might render a template for the main page
        return render_template('index.html')

@app.route('/toggle', methods=['POST'])
def toggle():
    config.toggle_variable = not config.toggle_variable
    return 'Success'


@app.route('/updates')
def updates():
    def generate_updates():
        while True:
            # Generate the updated text and highlighted spoken match here
            full_book_text = config.html_text#.replace('\n', '<br>')

            # Create a dictionary with the data to be sent
            data = {
                "full_book_text": full_book_text,
                "start": config.start_position,
                "end": config.end_position,
            }

            # Yield the SSE-formatted response
            yield f"data: {json.dumps(data)}\n\n"

    return Response(generate_updates(), mimetype='text/event-stream')


@app.route('/gpt_updates')
def gpt_updates():
    def generate_gpt_updates():
        while True:
            # Generate the updated GPT-4 output here
            updated_gpt_output = config.gpt_output

            # Yield the SSE-formatted response
            yield f"data: {updated_gpt_output}\n\n"

    return Response(generate_gpt_updates(), mimetype='text/event-stream')


@app.route('/highlight_updates')
def highlight_updates():
    def generate_highlight_updates():
        while True:
            # Generate the updated text and highlighted spoken match here
            full_book_text = config.html_text#.replace('\n', '<br>')

            # Create a dictionary with the data to be sent
            data = {
                "full_book_text": full_book_text,
                "start": config.start_position,
                "end": config.end_position,
            }

            # Yield the SSE-formatted response
            yield f"data: {json.dumps(data)}\n\n"

    return Response(generate_highlight_updates(), mimetype='text/event-stream') 


@app.route('/select_book', methods=['GET', 'POST'])
def select_book():
    if request.method == 'POST':
        selected_book = request.form.get('book')
        # Returns True if the checkbox is checked, False otherwise
        already_read = 'readBefore' in request.form 
        if already_read:
            config.read_before = 'previously'
        else:
            config.read_before = 'not previously'
        # get child's age
        config.age = int(request.form.get('childAge'))
        get_age_guidance()
        # get book text
        if selected_book == 'book_not_found' or selected_book == '':
            config.selected_book = ' '  # Set the selected book to an empty string or None
            config.book_text = ' '  # Set the book text to an empty string or None
            config.html_text = ' '  # Set the HTML text to an empty string or None
            config.have_book = False
        else:
            config.selected_book = selected_book
            config.book_text = get_book_text(config.selected_book)
            config.html_text = config.book_text
        return redirect(url_for('index'))
    else:
        with sqlite3.connect(config.database_path) as conn:
            c = conn.cursor()
            c.execute('SELECT name FROM files')
            books = [row[0] for row in c.fetchall()]
        return render_template('select_book.html', books=books)
    

@app.route('/search_books', methods=['POST'])
def search_books():
    search_text = request.form.get('search_text', '').strip().lower()
    with sqlite3.connect(config.database_path) as conn:
        c = conn.cursor()
        c.execute('SELECT name FROM files')
        books = [row[0] for row in c.fetchall() if search_text in row[0].lower()]
    return jsonify({'books': books})

@app.route('/popup_updates', methods=['GET'])
def popup_updates():
    def generate():
        while True:
            if config.generating:
                yield "data: Show\n\n"
            else:
                yield "data: Hide\n\n"
            time.sleep(0.5)

    return Response(generate(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(port=6050, use_reloader=False)

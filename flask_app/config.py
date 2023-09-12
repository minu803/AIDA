import queue
import numpy as np

break_threads = False # to quit out

#* recording audio variables *#
toggle_variable = False # toggle audio recording button
sample_rate = None # microphone sample rate, currently read by the audio recorder

#* question generation variables *#
text_all = "" # full transcription so far
gpt_output = "" # to store GPT output
sentence_counter = 0 # how many pages we've read - to decide when to generate q's
genmin = 2
genmax = 4
gen_counter = 3 # ask q's every gen_counter phrases. Start with 3
num_qs = 2 #num of questions to generate

#* transcript matching variables *#
score_threshold = 80 # threshold needed for transcript match
min_wordmatch = 5 # mimumum length of transcription to qualify for matching

#* global variables to hold and display the book text *#
book_text = '' # full book text (from database)
book_text_prev = '' # book text up until where we've read
html_text = '' # book text for display, includes highlighted markers
# mark start and end position of highlight / transcript match region
start_position = 0
end_position = 0 

#* Selections on startup page *#
selected_book = ''
have_book = True # for if we don't have the book
read_before = False
age = ''
age_guidances = ''

generating = False # toggle popup when generating q's

#* Queues *#
# Audio queue stores audio data from mic/recorder
audio_queue  = queue.Queue()
# Result queue stores transcribed output
result_queue = queue.Queue()
# transcript_queue stores the transcript to make questions from
transcript_queue = queue.Queue()

# editable variables
database_path = #
pdf_path = #
api_key = #

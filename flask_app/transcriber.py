
# import necessary packages
import speech_recognition as sr # https://pypi.org/project/SpeechRecognition/
import queue
from flask import Flask, render_template, Response
import time
import threading
import sys
import openai
import numpy as np
from fuzzywuzzy import fuzz
import argparse
import config

# Transcribe audio with WHISPER
def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file, language='en', 
                                             prompt="Children's story")
    return transcript["text"]

# Get audio data stored in audio_queue
# Pulls data from the queue that was put there with record_callback()
# Will pull data until queue is empty or (elapsed-time > min_time)
def get_all_audio(min_time=-1):
    audio = bytes()
    got_audio = False
    time_start = time.time()
    while not got_audio or time.time() - time_start < min_time: # min time unused right now
        # loops as long as there's something in the audio queue
        while not config.audio_queue.empty():
            audio += config.audio_queue.get() # pull data from audio queue
            got_audio = True

    data = sr.AudioData(audio,config.sample_rate,2)
    return data

# Get data from audio queue, save it as .wav, and transcribe .wav
# Adds transcribed .wav to result queue
def transcribe_data_from_queue():
    audio_data = get_all_audio() # get audio data from queue

    # Save audio data as .wav
    with open("latest.wav", "wb") as f:
        f.write(audio_data.get_wav_data())

    # Transcribe the saved audio file
    transcript_text = transcribe_audio('./latest.wav')

    # Add transcription to queue
    config.result_queue.put_nowait(transcript_text)


# Loop to run transcribe() in its own thread
# Continuosly grabs audio, transcribes it, and adds output to result queue
# status and break_threads need to be global?
def transcribe_loop():
    while True:
        if config.break_threads:
            break
        else:
            transcribe_data_from_queue()
    sys.exit()
    
    
def find_transcript_match(result):
    """
    Uses string edit distance to search for the closest match for transcript in the folder_path folder.
    @param transcript the text to search against our database for
    @param folder_path the folder that contains our book texts (stored as .txt)
    @return The highest similarity by edit distance, the closest match substring, and the path to the closest match
    """
    best_match_score = 0
    closest_match_text = None

    # generate word lists from full strings to do word-level matching
    book_text_byword = config.book_text.split(' ')
    book_text_byword = [word for word in book_text_byword if word != '']
    result_byword = result.split(' ')

    n = len(book_text_byword)
    m = len(result_byword)
    
    # Compute similarity score between transcript and document
    # similarity = fuzz.partial_ratio(transcript, file_content) This is better optimized, but doesn't get the substring achieving max score
    # using brute force, sliding window approach
    scores = []
    for i in range(n - m + 1):
        substring = book_text_byword[i:i+m]
        score = fuzz.ratio(substring, result_byword)
        scores.append(score)
        if score > best_match_score:
            best_match_score = score
            closest_match_text = (' ').join(substring)
            substring_start = i
            substring_end = i+m
    
    # make sure highest score is unique
    best_scores = np.where(np.array(scores) == best_match_score)[0]

    # if there is no unique maximum score, don't select a match
    if len(best_scores) > 1:
        if np.max(np.diff(best_scores)) > 1: # ok if the max scores are clustered
            closest_match_text = None
    # if there is no sufficiently high match, don't select a match
    if best_match_score < config.score_threshold:
        closest_match_text = None
        
    if closest_match_text is not None:
        config.start_position = substring_start
        config.end_position = substring_end
        str_before = (' ').join(book_text_byword[0:substring_start]).replace('. ', '.<br>')
        str_after  = ' ' + (' ').join(book_text_byword[substring_end:len(book_text_byword)]).replace('. ', '.<br>')
        str_middle = closest_match_text.replace('. ', '.<br>')
        html_text = str_before + '<mark>' + str_middle + '</mark>' + str_after
        config.html_text = html_text
        config.gpt_output = ''
        config.book_text_prev = str_before 

    return closest_match_text

    
# Loop to pull results and print it
# Continuosly grabs transcribed from result_queue and prints it
# result_queue, text_all, break_threads need to be global?
def print_result_loop():
    while True:
        result = config.result_queue.get() # get data from result queue
        print(result)
        if config.have_book:
            if len(result.split(' ')) >= config.min_wordmatch:
                transcript_match = find_transcript_match(result)
            if transcript_match is not None:
                config.transcript_queue.put_nowait(transcript_match)
                config.sentence_counter += 1
            print("Matching transcript: " + str(transcript_match))
        else:
            str_before = config.text_all
            str_middle = result
            html_text = str_before + '<mark>' + str_middle + '</mark>'
            config.html_text = html_text
            config.gpt_output = ''
            config.book_text_prev = str_before
            config.transcript_queue.put_nowait(result)
            
        config.text_all += result

        # If output result string too long, reset it
        #if len(text_all) > 2000:
        #    text_all = ""

        # Quit if 'stop' is said
        # need better way to quit threads?
        if result.lower().find('stop') > -1:
            #text_all += '. breaking...'
            config.break_threads = True
            break
    sys.exit()

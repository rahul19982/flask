from flask import Flask, render_template, request
import speech_recognition as sr
from os import path
from pydub import AudioSegment
import paralleldots
import json
import os
paralleldots.set_api_key("XXXXXXXX")
app = Flask(__name__)

@app.route('/')
def my_form():
   return render_template('hp.html')

@app.route('/result',methods = ['POST'])
def my_form_post():
   if request.method == 'POST':
      result = request.form['impath']
      files = os.listdir(result)
      for item in files:
        AUDIO_FILE = result + str(item)
        #name = item.split('.')
        ##print(name[0])
        #fh = open("recognized.txt", "w+") 
        #AUDIO_FILE = "/home/samroadie/Desktop/codebreak/audios/data/preamble1.wav"
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file
        text=r.recognize_google(audio)
        lang_code="en"
        response=paralleldots.sentiment(text,lang_code)
        return response

if __name__ == '__main__':
   app.run(debug = True)

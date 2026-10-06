import os
from random import random

import win32com.client
import speech_recognition as sr
import webbrowser
import openai
#from config import apikey
import datetime
import random
from httpx2 import query

def say(text):
    speaker=win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
       # r.pause_threshold=1
        audio =r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language="en-in")
            print(f"User said : {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry from Jarvis"


if __name__=='__main__':
    print('PyCharm')
    say("Hello I am JARVIS A I")
    while True:
       print("Listening...")
       query=takeCommand()
       sites=[["Youtube","https://www.youtube.com"],["wikipedia","https://wikipedia.com"],
              ["google","https://www.google.com"],["facebook","https://www.facebook.com"],
              ["instagram","https://www.instagram.com"]]
       for site in sites:
          if f"Open {site[0]}".lower() in query.lower():
           say(f"Opening{site[0]}  sir.....")
           webbrowser.open(site[1])

       if "play music" in query:
          musicpath="C:/Users/vikas/Music/Aaj Bhi Vishal Mishra 320 Kbps.mp3"
          os.startfile(musicpath)

       if "the time" in query:
           strTime =datetime.datetime.now().strftime("%H:%M:%S")
           say(f"The time is {strTime}")
       # if "open jio hotstar".lower() in query.lower():
       #     os.system((f"open C:/Program Files/BlueStacks_nxt"))


       # #say(query)





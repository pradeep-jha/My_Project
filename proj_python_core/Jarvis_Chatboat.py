import pyttsx3
import speech_recognition as sr
import pyaudio
from win32com.client import Dispatch
import datetime
import time
import os
import webbrowser


# from decouple import config

def speak(str):
    speak = Dispatch("SAPI.spVoice")
    speak.Speak(str)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said :{query}\n")
    except Exception as e:
        print(e)
        print("Say that again please..")
        return "None"
    return query
if __name__=="__main__":
    audio=takeCommand()
    if "time" in str.lower(audio):
        time_12 = time.strftime("%I:%M %p")
        #time_12_h_m_s = time.strftime("%I:%M:%S %p")
        print(time_12)
        speak(f"The current time is: {time_12}")
        audio = takeCommand()
        #speak(time_12)
    elif "music" in str.lower(audio):
        music_dir="E:\songs"
        songs=os.listdir(music_dir)
        print(songs)
        print(songs[10])
        os.startfile(os.path.join(music_dir,songs[10]))
        time.sleep(10)
        audio = takeCommand()
    elif "google" in str.lower(audio):
        webbrowser.open("google.com")
        time.sleep(10)
        audio = takeCommand()
    elif "youtube news" in str.lower(audio):
            speak("opening republic news in youtube")
            webbrowser.open("https://www.youtube.com/watch?v=ckKA-0MUm4E")
            time.sleep(10)
            audio = takeCommand()


import pyttsx3
import speech_recognition as sr
import pyaudio
from win32com.client import Dispatch
import datetime
import time
import os
import webbrowser
import random
from proj_python_core import Teprature_calculaor

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
        print("I am sorry! Say that again please..")
        #speak("I am sorry! Say that again please..")
        return "None"
    return query
if __name__=="__main__":
    while True:
        speak("Hi There! How may I help you")
        audio=takeCommand()
        if "time" in str.lower(audio):
            time_12 = time.strftime("%I:%M %p")
            #time_12_h_m_s = time.strftime("%I:%M:%S %p")
            print(time_12)
            speak(f"The current time is: {time_12}")
        elif "audio" in str.lower(audio):
            music_dir="E:\songs"
            songs=os.listdir(music_dir)
            #print(songs)
            audio_songs = []
            for song in songs:
                if (song[len(song) - 3:] == "mp3"):
                    audio_songs.append(song)
            print(audio_songs)
            n = random.randint(0, len(audio_songs)-1)
            print("song number: ",n)
            song_name_noext = audio_songs[n][:len(audio_songs[n])-4]
            print(song_name_noext)
            song_name=audio_songs[n]
            print(song_name)
            speak(f"opening the audio song {song_name_noext}  from local folder")
            os.startfile(os.path.join(music_dir, song_name))

        elif "video" in str.lower(audio):
            music_dir="E:\songs"
            songs=os.listdir(music_dir)
            #print(songs)
            vedio_songs = []
            for song in songs:
                if (song[len(song) - 3:] == "mp4"):
                    vedio_songs.append(song)
            print(vedio_songs)
            n = random.randint(0, len(vedio_songs)-1)
            print("song number: ", n)
            song_name_noext = vedio_songs[n][:len(vedio_songs[n]) - 4]
            print(song_name_noext)
            song_name = vedio_songs[n]
            print(song_name)
            speak(f"opening the video song {song_name_noext}  from local folder")
            os.startfile(os.path.join(music_dir, song_name))

        elif "google" in str.lower(audio):
            speak("opening google in internet explorer!")
            webbrowser.open("google.com")
            # time.sleep(10)
            # audio = takeCommand()
        elif "youtube news" in str.lower(audio):
                speak("opening republic news in youtube")
                webbrowser.open("https://www.youtube.com/watch?v=ckKA-0MUm4E")
        elif "playlist" in str.lower(audio):
                speak("opening  songs from your playlist in youtube")
                webbrowser.open("https://www.youtube.com/watch?v=m4wzXcfbkOQ&list=PLGsuPLNadTJLEOByd1rQs2mG9AUIH9Jj9")
        elif "notepad" in str.lower(audio):
                speak("opening a new Notepad")
                os.startfile("C:\\Users\\pradeep\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad")
        elif "excel" in str.lower(audio):
                speak("opening a new excel spreadsheet")
                os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Excel 2013")
        elif "quick note" in str.lower(audio):
            speak("opening a new quick note")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Excel 2013")

        elif "ppt" in str.lower(audio):
                speak("opening a new Power point presentation")
                os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\PowerPoint 2013")
        elif "word" in str.lower(audio):
                speak("opening a new MS word file")
                os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013")
        elif "presentation" in str.lower(audio):
                speak("opening hadoop presentation")
                os.startfile("C:\\Users\\pradeep\\Desktop\\python_autmation_codes\\ppt_sample\\Hadoop.pptx")
        elif "headlines" in str.lower(audio):
                os.startfile("C:\\Users\\pradeep\\Desktop\\News_Reader.exe")
        elif "weather" in str.lower(audio):
                speak("please tell the city name")
                city = takeCommand()
                city_name = str.lower(city)
                if city_name !='none':
                    print("city name is :",city_name)
                    try:
                        weather = Teprature_calculaor.get_weather(city_name)
                        speak(weather)
                    except Exception as e:
                        #speak("got am exception")
                        #print(e)
                        speak(f"{city_name} is not a correct city name")
                        speak("please tell the correct city name")
                        try:
                            city = takeCommand()
                            city_name = str.lower(city)
                            if city_name != 'none':
                                print("city name is :", city_name)
                                weather = Teprature_calculaor.get_weather(city_name)
                                speak(weather)
                        except Exception as e:
                            speak("No correct city name found! Taking you to main menu...")
                            speak("........")
                            #audio = takeCommand()
                        # speak("I am sorry! Say that again please..")
        elif "stop" in str.lower(audio):
                speak("THANK YOU ! JARVIS shutting down!")
                exit()
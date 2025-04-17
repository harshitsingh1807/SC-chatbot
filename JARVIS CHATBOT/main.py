import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os



recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    pygame.mixer.init()

    pygame.mixer.music.load('temp.mp3')

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    client = OpenAI(api_keys="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")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please "},
            {"role":"user","content" : command}
        ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
    elif "open hotstar" in c.lower():
        webbrowser.open("https://www.hotstar.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://web.instagram.com")
    elif "open amazon" in c.lower():
        webbrowser.open("https://www.amazon.com")
    elif "open flipkart" in c.lower():
        webbrowser.open("https://www.flipkart.com")
    elif "open amazon" in c.lower():
        webbrowser.open("https://www.amazon.com")
    elif "open zomato" in c.lower():
        webbrowser.open("https://www.zomato.com")
    elif "open telegram" in c.lower():
        webbrowser.open("https://www.telegram.com")
    elif "open netflix" in c.lower():
        webbrowser.open("https://www.netflix.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    else:
        output=aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2 )
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
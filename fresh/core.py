#!/usr/bin/env python3
"""
This project aims to provide basic AI functionality,
along with any dumb ideas or features that we
mindlessly add without need.

Significant code has been "inspired" by examples
found online.

Authors = Ben Rose, James 'Poo Head' Dibnah
"""

#imports
import speech_recognition as sr
import sys

def main():
    #intro
    print("Welcome to the future!")

    #run the dumb shizzle
    while True:
        parse(listen())


def listen():
    #take in audio and pump it through sr
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Sup")
        audio = recog.listen(source)

    # recognize using Google API
    try:
        print("Google thinks you said: " + recog.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google is fucking dumb and can't understand you.")
    except sr.RequestError as e:
        print("Google just cba; {0}".format(e))

def parse(recogInput):
    #this understands the recognized text



main()

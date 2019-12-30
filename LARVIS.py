from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pyttsx3 as pyttsx3
import speech_recognition as sr
import os
import sys
import re
import webbrowser
import subprocess
import smtplib
import wikipedia
from random import randrange
from time import strftime
import wolframalpha
import pytz
import requests

"""
    Create By Lidor Eliyahu S.
    All rights reserved
    Please see README.txt for instructions
"""

# SCOPES = []   Get this from https://developers.google.com/calendar/quickstart/python
MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november",
          "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]
CALENDAR_OPTIONS = ["what do i have", "do i have plans", "am i busy"]
NOTE_OPTIONS = ["make a note", "write this down", "remember this"]


def larvis_response(audio):
    print(audio)
    response = pyttsx3.init()
    voices = response.getProperty('voices')
    response.setProperty('voice', voices[2].id)
    response.say(audio)
    response.runAndWait()


def larvis_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....ERROR....')
        command = larvis_command()
    return command.lower()

























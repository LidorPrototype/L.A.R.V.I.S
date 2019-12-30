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
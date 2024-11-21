# Exercise 9_ Solution - Shoutouts to Everyone

# for mac
'''
from os import system
names = ["Hammad", "Ammarah", "Ali", "Haseeb"]
for name in names:
    system(f'say Shoutout to {name}')
'''

import win32com.client

shoutout = ["Hammad", "Ammarah"]

speaker = win32com.Dispatch("SAPI.SpVoice")

for name in shoutout:
    s = name
    speaker.Speak(f"Shoutout to {name}")

# Another way of doing the above

import pyttsx3

shoutout =  ["Hammad", "Ammarah"]

# Initialize the text-to-speech

engine = pyttsx3.init()

# Loop through the names in the shoutout list and speak each one

for name in shoutout:
    engine.say(f"Shoutout to {name}")
    engine.runAndWait()
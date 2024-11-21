import datetime
import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

current_hour = datetime.datetime.now().hour

if 5 <= current_hour < 12:
    greeting = "Good morning!"
elif 12 <= current_hour < 18:
    greeting = "Good afternoon!"
else:
    greeting = "Good night!"

# Say the greeting aloud
engine.say(greeting)
engine.runAndWait()

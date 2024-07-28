# Install an external module and use it to perform an operation of your interest
# Copied from Usage of ppttsx3 : https://pypi.org/project/pyttsx3/
import pyttsx3
engine = pyttsx3.init()
engine.say("Hey, This is me, Hunter. I am currently learning Python from Code With Harry")
engine.runAndWait()
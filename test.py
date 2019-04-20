
#Importing Windows Speaking Agent male SAPI
#Both code works on windows only
#However same code is working on my local machine

#1st Method
#first install pyttsx3 windows
#pip install pyttsx3

import pyttsx3 
# initialisation 
engine = pyttsx3.init() 
# testing 
engine.say("I am working Jenkins") 
engine.say("Test") 
engine.runAndWait() 
'''
#2nd Method
import time
#Default speaking agent no need to install anything apart from python 3.6.6.
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")
time.sleep(2)
#Your Laptop speaker should speak the sentence in quotes this is not working
speak.Speak("Hi This is Test")
'''
print('Message from Git')

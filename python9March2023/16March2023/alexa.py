import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener=sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Start Speaking!")
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        command=command.lower() 
        if 'alexa' in command:
            print(command)
except:
    pass
        
    
# engine=pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)


# def talk(text):
#     engine.say(text)
#     engine.runAndwait()
# info=wikipedia.summary(person,1)
# print(info)
# talk(info) 
# def take_command():
#     print("hii")
from gtts import gTTS
import speech_recognition as sr
from pygame import mixer
import re
import webbrowser
import random

def whisper(audio):
    print(audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang='en-uk')
        text_to_speech.save('audio.mp3')
        mixer.init()
        mixer.music.load('audio.mp3')
        mixer.music.play()


# whisper('Hey I am Swapy! How you dey?')


# function that will listen for commands
def listen():
    #Initialize the recognizer
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Visis is Ready...')
        r.pause_threshold = 1
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source, duration=1)
        #listens for the user's input
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = listen()

    return command


    

# listen()

# def vivi(command):
#     errors=[
#     'I don’t know what you mean!',
#     'Excuse me?',
#     'Can you repeat it please?',
#     ]
#     if 'Hello' in command:
#         whisper('Hello! I am Visis. How can I help you?')

#     else:
#         error = random.choice(errors)
#         whisper(error)


# vivi('Visis is ready!')
# while True: listen()


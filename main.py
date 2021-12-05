import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
seemee = pyttsx3.init()
voices = seemee.getProperty('voices')
seemee.setProperty('voice', voices[1].id)


def talk(text):
    seemee.say(text)
    seemee.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'seemee' in command:
                command = command.replace('seemee', '')
    except:
        pass
    return command


def run_seemee():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'love' in command:
        talk('Sorry, I have no idia about love')
    else:
        talk('I did not get it but I can search it for you')
        pywhatkit.search(command)


while True:
    run_seemee()

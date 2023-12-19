import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()


def assistant_speak(message):
    print(message)
    engine.say(message)
    engine.runAndWait()


def cmd():
    assistant_speak("Hello!")
    assistant_speak("How can I help you?")

    with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Listening...')
        recordedaudio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(recordedaudio, language='en_US')
        text = text.lower()
        print('Your message:', format(text))

        if 'bye' in text:
            assistant_speak('Goodbye!')
            exit()

    except Exception as ex:
        print(ex)
        text = ''  # Initialize text with an empty string if an exception occurs

    if 'chrome' in text:
        assistant_speak('Opening Chrome...')
        programName = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])
    elif 'time' in text:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(current_time)
        assistant_speak(current_time)
    elif 'play' in text:
        assistant_speak('Opening YouTube...')
        pywhatkit.playonyt(text)
    elif 'youtube' in text:
        assistant_speak('Opening YouTube...')
        webbrowser.open('https://www.youtube.com')


while True:
    cmd()
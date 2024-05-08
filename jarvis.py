import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
# import openai


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate= engine.getProperty('rate')
engine.setProperty('rate',150)



def say(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        say("Good Morning sir!")
    elif 12 <= hour < 18:
        say("Good Afternoon sir!")
    else:
        say("Good Evening sir!")
    say("Hello, I am debjit. How may I help you?")


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        say("Sorry, I didn't catch that. Please repeat.")
        return ""
    except sr.RequestError:
        say("Sorry, there was an issue with the speech recognition service.")
        return ""

if __name__ == '__main__':
    wish()

    query = listen()

    if 'wikipedia' in query.lower():
        say('Searching Wikipedia....')
        query = query.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=5)
            say("According to Wikipedia")
            print(results)
            say(results)
        except wikipedia.exceptions.DisambiguationError as e:
            say("There are multiple possible results. Please be more specific.")
            print("DisambiguationError:", e)
        except wikipedia.exceptions.PageError as e:
            say("Sorry, I couldn't find any relevant information.")
            print("PageError:", e)

    elif 'play in youtube' in query.lower():
        say('Searching in YouTube....')
        query = query.replace("play in youtube", "")
        webbrowser.open("https://www.youtube.com/results?search_query=" + query)

    elif 'open google' in query.lower():
        webbrowser.open("https://www.google.com")

    elif 'open stackoverflow' in query.lower():
        webbrowser.open("https://www.stackoverflow.com")

    elif 'play in spotify' in query.lower():
        say('searching in spotify......')
        query = query.replace("spotify", "")
        webbrowser.open("https://open.spotify.com/search")

    elif 'what is the time now' in query.lower():
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"sir the time is {strtime}")

    elif 'open code' in query.lower():
        codePath = r"C:\Users\VICTUS\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        os.startfile(codePath)
        
            
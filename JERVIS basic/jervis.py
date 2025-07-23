import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser


engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    import datetime
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis, your personal assistant. How can I help you today?")    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I did not understand that.")
        return "None"
    
    return query

if __name__ == "__main__":
    wishMe()
    while True:
       query = takeCommand().lower()
       if 'wikipedia' in query:
           speak("Searching Wikipedia...")
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=5)
           speak("According to Wikipedia")
           print(results)
           speak(results)

       elif 'open youtube' in query:
            speak("Opening YouTube")
            import webbrowser
            webbrowser.open("https://www.youtube.com")
       elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
       
       elif 'open github' in query:
            speak("Opening GitHub")
            webbrowser.open("https://github.com")
       elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
       elif 'date' in query:
            strDate = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {strDate}")
       elif 'stop' in query or 'exit' in query:
            speak("Goodbye!")
            break
       else:
           speak("I am not sure how to help with that.")                           
# pip install pyttsx3
import pyttsx3
# pip install SpeechRecognition
import speech_recognition as sr
import datetime
# pip install wikipedia
import wikipedia
# importing for youtube directly
import webbrowser

engine = pyttsx3.init('sapi5')  # Microsoft gives the voices inbuilt
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # voice 0 for male, 1 for female


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis sir. Speed 1 terahertz, memory 1 zettabyte. Command mode activated. Please tell me how may I help you?")


def takeCommand():
    # It takes input from the user and returns a string as output
    r = sr.Recognizer()  # speech recognizer
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"

    return query


def calculate(query):
    try:
        query = query.replace('calculate', '').strip()
        query = query.replace('plus', '+')
        query = query.replace('minus', '-')
        query = query.replace('into', '*')
        query = query.replace('divided by', '/')
        query = query.replace('into', '*')
        query = query.replace('and', '')  # query "calculate 5 plus 2"
        result = eval(query)
        speak(f"The result is {result}")
        print(f"Calculation result: {result}")
    except Exception as e:
        speak("Sorry, I couldn't perform the calculation. Please try again.")
        print("Calculation error:", e)


if __name__ == "__main__":
    wishMe()
    time_spoken = False  # Flag to track if the time has been spoken
    while True:
        query = takeCommand().lower()
        # logic for executing various tasks

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open teams' in query:
            webbrowser.open('https://teams.microsoft.com/v2/')
        elif 'open academia' in query:
            webbrowser.open('https://erp.dituniversity.edu.in/#')
        elif 'tell time' in query:
            if not time_spoken:
                time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {time}")
                time_spoken = True  # Set flag to True after speaking the time
        elif 'calculate' in query:
            calculate(query)
        elif 'jarvis exit' in query or 'quit' in query:
            speak("Goodbye Sir, shutting down.")
            break

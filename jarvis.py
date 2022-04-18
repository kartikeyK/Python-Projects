import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices[1].id)
engine.setProperty("voice",voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good morning!")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak("I am jarvis. Please tell me how can i help you?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User said: ", query)

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("kartikeykainthola@gmail.com", "Heisenberg@0987654321")
    server.sendmail("kartikeykainthola@gmail.com", to, content)
    server.close

if __name__ == "__main__":
    wishme()
    takecommand()
    while True:
    #if 1:
        query = takecommand().lower()

    #Logic for tasks according to the query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open agario' in query:
            webbrowser.open("agar.io")


        elif 'play music' in query:
            music_dir = 'C:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            print(strTime)

        elif 'send email' in query:
            try:
                speak("Please tell me your message?")
                content = takecommand()
                to = "hitesh_aswani@hotmail.com"
                sendEmail(to, content)
                speak("Your Email has been sent!")
                print("Your Email has been sent!")
            except Exception as e:
                #print(e)
                speak("Sorry my friend. i am not able to send this email.")

        
        elif 'bye' in query:
            speak("Good bye master.")
            print("Good-Bye!!!")
            exit
            break

        elif 'who is your Creator' or 'who created you' in query:
            speak("well,I dont know about earth. But my creator is master kartikey.")
            speak("He is new, but he made me.")
            print("Kartikey is my master") 
 
        
            
        
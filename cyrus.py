import sys

import pyttsx3
import speech_recognition as sr
from datetime import datetime
import os
import cv2
import wikipedia as wikipedia
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
# text to speech
def speak(audio):

    engine.say(audio)
    print(audio)
    engine.runAndWait()
# to convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            speak("Say that again please...")
            return"name"
        return query

# to wish
def wish():
    hour = int(datetime.now().hour)

    if hour>=0 and hour>=12:
        speak("hi dear,welcome")
    elif hour>12 and hour<18:
        speak("hi there ,welcome")
    else:
        speak("good evening")
    speak("i am heather . please tell me how can i help you")

# to send email
def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("your email id", "your password")
    server.send("your email id", to, content)
    server.close()

if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        # logic building for tasks

        if "open notepad" in query:
            npath = "C:\\windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open Excel" in query:
            npath = "C:\\Users\\Dell\\OneDrive\\Desktop"
            os.startfile(npath)

        elif"open command prompt" in query:
            os.system("start cmd")

        elif"open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif"ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
           # print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open twitter" in query:
            webbrowser.open("www.twitter.com")

        elif "how are you" in query:
            speak("i am good how are you")

        elif "what is the time" in query:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            speak("sir, current time is=", current_time)

        elif "who is your master" in query:
            speak("sir, you are my master and i am loyal to you")

        elif "do you have family" in query:
            speak("sir,you are my only family")

        elif "i am feeling sad" in query:
            speak("sir how can i help you")

        elif "what you are doing now" in query:
            speak("sir,just trying to help you out")

        elif "open google" in query:
            speak("sir,opening google....")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")


        elif "send message" in query:
            kit.sendwhatmsg("+919548691377", "this is testing program",16,20 )

        elif "play song on youtube" in query:
            kit.playonyt("sad songs")

        elif "email to vaibhav" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "chaudharyvaibhav184@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to vaibhav")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send to email to vaibhav")

        elif "no thanks" in query:
            speak("thanks for using me sir, have a nice day.")
            sys.exit()

        speak("sir, do you have any other work")







import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import pywhatkit

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("how are you Aadi")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)


# time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Today's date is")
    speak(date)
    speak(month)
    speak(year)

def month():
    month = int(datetime.datetime.now().month)
    speak("This Month is ")
    if(month ==1):
     speak("January")
    elif(month == 2):
        speak("Ferbruary")
    elif(month == 3):
        speak("March")
    elif(month == 4):
        speak("April")
    elif(month == 5):
        speak("May")
    elif(month == 6):
        speak("June")
    elif(month == 7):
        speak("July")
    elif(month == 8):
        speak("August")
    elif(month == 9):
        speak("September")
    elif(month == 10):
        speak("October")
    elif(month == 11):
        speak("November")
    elif(month == 12):
        speak("December")
           

# date()

def greet():
    speak("Welcome back sir")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    elif hour >= 18 and hour < 24:
        speak("good evening sir")
    else:
        speak("good night sir.Have a good sleep")
    speak("jarvis at your service. Please tell me how can i help you")


# greet()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        #r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Aadi Said:{query}\n")
    except Exception as e:
        print(e)
        speak("Sorry didn't get that")
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return query


# takeCommand()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)  # gmail uses port 587
    server.ehlo()
    server.starttls()
    server.login('rjk1999.18@gmail.com', 'pass')
    server.sendmail('rjk1999.18@gmail.com', to, content)
    server.close()


def remember():
    speak("what do you want me to remember sir")
    data = takeCommand()
    speak("You told me to remember that " + data)
    remember = open('remember.txt', 'w')
    remember.write(data)
    speak("I remember that now")
    remember.close()


def screenshot():
    image = pyautogui.screenshot()
    image.save("ss.png")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("the cpu is at " + usage)
    
    battery = psutil.sensors_battery()
    speak("the battery is at")
    speak(battery.percent)


def jokes():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)


if __name__ == "__main__":
    greet()
    while True:
        query = takeCommand().lower()

        if ('hey jarvis') in query:
            speak("hello sir,what can i do for you?")

        elif ('hello jarvis') in query:
            speak("hello sir,what can i do for you?")

        elif ('hello') in query:
            speak("hello sir,what can i do for you?")
            
        elif 'time' in query:
            time()

        elif 'date' in query:
            date()
            
        elif 'month' in query:
            month()

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'send mail' in query:
            try:
                speak("what am i supposed to send sir")
                content = takeCommand()
                to = 'slrjk.18@gmail.com'
                sendEmail(to, content)
                speak("email has been sent to ")
                speak(to)

            except Exception as e:
                print(e)
                speak("sorry sir ,couldn't send the mail")

        elif 'chrome search' in query:
            speak("what am i supposed to search sir?")
            search = takeCommand()
        #    print('google think you said:\n' + search + '.com')
         #   speak(search + "is this what you said sir")
          #  valid = takeCommand()
            chrome_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
            chrome = wb.get(chrome_path)
               #chrome.open('http://google.com')
            chrome.open_new_tab(search+ '.com')
         #   else:
          #      speak("can you repeat that once again sir")
           #     search = takeCommand()
            #    print('google think you said:\n' + search + '.com')
             #   chrome_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
              #  chrome = wb.get(chrome_path)
                #chrome.open('http://google.com')
               # chrome.open_new_tab(search+ '.com')

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play' in query:
            if 'play' in query:
                song = query.replace('play', '')
                speak('Playing'+ song )
                pywhatkit.playonyt(song)
            else:
                 speak("No songs found")

        elif 'remember' in query:
            remember()
            speak("do you want me to remember something new sir?")
            ask = takeCommand()
            if (ask == 'yes'):
                remember()
            else:
                quit()

        elif 'reminder' in query:
            rem = open('remember.txt', 'r')
            content = rem.read()
            if(os.path.getsize("remember.txt")==0):
                speak("you don't have any reminders yet.")
            else:
                print(content)
                speak("You have said me remember that " + content)

        elif 'take screenshot' in query:
            screenshot()
            speak("Done")
           # speak("do you want me to take another screenshot sir?")
            #ask = takeCommand()
            #if (ask == 'yes'):
             #   screenshot()
            #else:
             #   quit()
        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'exit' in query:
            speak("Ok sir exiting")
            quit()
        
        elif 'quit' in query:
            speak("Ok sir quiting")
            quit()
            
        elif 'close' in query:
            speak("Ok sir closing")
            quit()

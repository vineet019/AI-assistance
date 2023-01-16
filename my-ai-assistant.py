import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import gtts
from playsound import playsound
import pygame
import datetime
import sys
import random
import time
 


print('Loading your AI personal assistant - Telemoto X')

engine=pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-0)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.25)
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')



def speak (text):
       
    tts = gtts.gTTS(text)
    tts.save("hello.mp3")
    playsound("hello.mp3")
    gtts.gTTS(text)



#def speak(text):
    #engine.say(text)
    #engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning Vineet")
        print("Hello,Good Morning Vineet")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon Vineet")
        print("Hello,Good Afternoon Vineet")
    else:
        speak("Hello,Good Evening Vineet")
        print("Hello,Good Evening Vineet")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            #speak("Pardon me, please say that again")
            return "None"
        return statement

wishMe()
speak("Loading your AI personal assistant Telemoto-X")
speak("Tell me vineet how can I help you?")
#wishMe()

if __name__=='__main__':


    while True:
        statement = takeCommand().lower()
        
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Telemoto-X is shutting down,Good bye')
            print('your personal assistant Telemoto-X is shutting down,Good bye')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Telemoto-X your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Vineet")
            print("I was built by Vineet")

        elif "who is neda" in statement:
            speak("hummm...... , Acoording to Linked in, Neda is SVP at Stellantis, Neda previously work with vineet at Tesla")
            print("about Neda")

        elif "open the left window" in statement:
            speak("Do you want to open left window yes or No")
            statement = takeCommand().lower()
            time.sleep(3)

            if "yes" in statement:
                speak("Opening window now")
                time.sleep(0)

        elif "open the right window" in statement:
            speak("Do you want to open right window yes or No")
            statement = takeCommand().lower()
            time.sleep(3)

            if "yes" in statement:
                speak("Opening right window now")
                time.sleep(0)


        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")
            takeCommand()

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            
        elif "story" in statement:
            
            speak("Do you want me to tell you a story")
            statement = takeCommand().lower()
            time.sleep(3)

            if "yes" in statement:
                speak("here is a story from : Study.com - Dinosaur Story for Kids \n Once upon a time 210 million years ago the sun was shining as Sammy the Stegosaurus watched the pterodactyls flap their wings and fly above the treetops Wow she thought I have never seen a dinosaur that flies before! She could not believe that pterodactyls wingspan can be as large as 30 feet. It looked like fun, but it made Sammy feel frustrated and sad. She was a stegosaurus and could not fly. She did not have any friends to play with. Tippy the Pterodactyl saw Sammy crying and flew down to the forest to talk to her. Tippy landed and was walking on all fours, unlike other birds Sammy had seen. Sammy was excited that a new friend was coming to her. She thought she might finally have a friend to play with. Hi I m Sammy. Do you want to play a game with me over here?Sammy asked. Tippy replied, I dont want to play down here. I want to soar in the sky. Why cant you just fly up here and play with us? I cant. I cant fly. I am a stegosaurus. Sammy replied. You dont know how to fly?! That is so weird! And what are those pointy things on your back? I only play games up in the sky with my pterodactyl friends. Before Sammy could tell her about all 17 bony plates that pointed out like spikes and ran down her back in two rows, Tippy had already started to fly away. Sammy could hear her laughing in the distance.")
                time.sleep(0)
        
        elif "check my calendar" in statement:
            
            speak("You have -- 9 am Meeting with Sam: 11 am O2 Club Meeting : 12 pm Lunch with Neha : 2 pm Pickup Lizzy")
            statement = takeCommand().lower()
            time.sleep(3)

        elif "emergency" in statement:
            
            speak("Do you want me to call your emergency contacts?")
            statement = takeCommand().lower()
            time.sleep(3)
            
            if "yes" in statement:
                speak("Calling your emergency contact")
                time.sleep(1)
            elif "no" in statement:
                speak("No worries my bad")
                
            else :
                speak("Pardon me, please say that again")
                
                time.sleep(1)
                
        elif "thankyou" or "you are great" in statement:
            speak("its my pleasure")
            time.sleep(0)
            takeCommand()
        
        elif "telemoto" in statement:
            speak("hi vineet how ma i help")
            time.sleep(0)
            takeCommand()  
            
            

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
              
        

time.sleep(3)













import socket
import requests, json
import urllib.request, json
from bs4 import BeautifulSoup
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys
import re
import subprocess
from googlesearch import search
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot('Bot')
trainer = ListTrainer(chatbot)
socket.getaddrinfo('localhost','8080')
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)



def speak(audio):
    audio=str(audio)
    print('Bot: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir')
speak('How may I help you?')
speak("I can also do web search for you query. \n for that you need to type web")

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except Exception:
        speak('Sorry sir! I didn\'t get that! Try typing ....')
        query = str(input('User: '))

    return query

def GoogleForm():
    speak("I am sorry to hear that. \nokay.. now no need to worry. ")
    speak("i am here to help you.")
    speak("what is you name")
    name = myCommand()
    speak("what is you Phone Number")
    phno = myCommand()
    speak("okay..now please give me more details for you problem")
    body = myCommand()
    speak("your problem has been sucessfully registered...\n our team contact you as soon as posible and they will help you to solve your problem on {} ".format(body))


def GoogleForm1():
    speak("I felt bad to hear that. \nokay.. now no need to worry. ")
    speak("i am here to help you.")
    speak("what is you name")
    name = myCommand()
    speak("which company against you want to send to send your problem")
    comp=myCommand()
    recip=comp+"@gmail.com"
    #phno = myCommand()
    speak("okay.. please tell me more about your problem")
    body = myCommand()
    mailsent(recip,body)
    speak("your problem has been sucessfully registered...\n our team contact you as soon as posible and they will help you to solve your problem on {} ".format(body))

def focus():
    speak("I felt bad to hear that. \nokay.. now you  don't need to worry about. ")
    speak("i am here to help you.")
    speak("what is you name")
    name = myCommand()
    speak("what is your location if you don't know then type nearby shop name")
    loc = myCommand()
    recip="rescuedept@gmail.com"
    speak("okay..now please give me some more detail .. what did you see")
    body = myCommand()
    speak("your urgent help has been sucessfully registered...\n we are sending our team which will help you to solve your problem on {} ".format(body))
    body=body+"my location is {}".format(loc)
    mailsent(recip,body)


    
def mailsent(recip,body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    print("reached gmail")
    server.ehlo()
    server.starttls()
    server.login("salman19121141@gmail.com", password())
    print("loged In")
    server.sendmail('salman19121141@gmail.com', recip, body)
    server.close()
    speak('Email has been sent successfuly. You can check your inbox.')


def GoogleMap():
    z=open("F:\\others\\Compressed\\s1.txt", "r")
    content1 =z.read()
    
    api_key = content1

    # url variable store url 
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    # get method of requests module 
    # return response object 
    r = requests.get(url + 'query=' + query +'&key=' + api_key) 
    # json method of response object convert 
    # json format data into python format data 
    x = r.json() 
    print(x)

def password():
    z=open("F:\\others\\Compressed\\s.txt", "r")
    content1 =z.read()
    return content1
        

if __name__ == '__main__':
    
    #speak("please choose \n1.ONLINE mode \n2.OFFLINE mode")
    qr = 1
    while True:
    
        query = myCommand();
        query = query.lower()
        qan=query.find("wh")
        l=query.count(" ")


        
        if ('problem' in query) or ('issue' in query) or ('trouble' in query) or ('difficulty' in query) or ('complaint' in query):
            try:
                GoogleForm()
            except:
                speak("i am sorry sir... there is some connection problem. You can try after sometimes...")
            
        elif ('not working' in query) or ('not coming' in query) or ('trouble' in query) or ('repair' in query) or ('renovation' in query) or ('restore' in query) or ('refund' in query):
            try:
                GoogleForm1()
            except:
                speak("i am sorry sir... there is some connection problem. You can try after sometimes...")

        elif ('accident' in query) or ('disaster' in query) or ('trouble' in query) or ('damage' in query) or ('urgent help' in query) or ('hazard' in query) or ('coincidence' in query) or ('ambulance' in query):
            try:
                focus()
            except:
                speak("i am sorry sir... there is some connection problem. You can try after sometimes...")
            


        elif 'help me' in query or 'can you do' in query:
            speak("""I can help you in many ways like :
                  
                  1.  All type of residential problem
                  2.  Help to find out best result for your query
                  3.  Show to you all the services nearby you 
                  4.  Open any website for example google.com
                  5.  Send Email 
                  6.  tell me about xyz for example tell me about Taj Mahal
                  7.  Helps to control all disaster
                  8.  Provides all the complaint facility
                  9.  Play a music for you.
                  10. Open any important application in your system
                  
                  """)
        
        elif 'nearby' in query :
            try:
                GoogleMap()
            except:
                speak("i am sorry... there is some connection problem. You can try after sometimes...")
            
        
            
        elif 'open youtube' in query :
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif '.com' in query:
            speak('okay')
            regx=re.search('open (.+)',string=query)
            domain=regx.group(1)
            print(domain)
            url='https://www.'+domain
            
            print(query)
            webbrowser.open(url)

        elif ('launch' in query) or ('open' in query) :
            try:
                print('okay')
                regx=re.search('open (.+)',string=query)
                domain=regx.group(1)
                #print(domain)
                t="C:\\Users\\Salman Sheikh\\Desktop\\application\\"+domain
                os.startfile(t)
            except:
                speak("I have only these applications permission to open...")
                t=os.listdir("C:\\Users\\Salman Sheikh\\Desktop\\application")
                for i in t:
                    speak(i)
                


        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            
            try:
                speak('What should I say? ')
                content = myCommand()
        
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login("salman19121141@gmail.com", password())
                server.sendmail('salman19121141@gmail.com', recipient, content)
                server.close()
                speak('Email has been sent successfuly. You can check your inbox.')

            except:
                speak('Sorry Sir! I am unable to send your message at this moment!....\n please try again later')


        elif 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'who is your' in query:
            result=chatbot.get_response(query)
            result=str(result)
            speak(result)

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'tell me about' in query:
            results = wikipedia.summary(query, sentences=2)
            speak("Searching....")
            speak('Got it.')
            speak('WIKIPEDIA says - ')
            speak(results)
            
        elif 'play music' in query:
            music_folder = 'F:\Songs\Music\Salman'
            songs=os.listdir(music_folder)
            random_music = music_folder + random.choice(songs)
            os.startfile(os.path.join(music_folder,random.choice(songs)))
                  
            speak('Okay, here is your music! Enjoy!')


        elif l<=2:
            result=chatbot.get_response(query)
            result=str(result)
            speak(result)

        elif qan!=0: 
            try:
                url = "http://www.google.de/search?q="+ query
                for url in search(query, stop=3):
                    print(url)
                    page=urllib.request.urlopen(url)
                    soup=BeautifulSoup(page,"lxml")
                    print(soup.head.title.contents)
                    tags=soup.findAll('p')
                    print(tags[0].contents)
            except:
                speak('Sorry Sir! there is some temporary connection problem at this moment!....\n please try again later')
                

        elif 'web' in query or (qan==0):
            try:
                if 'web' in query:
                    speak("what you want to search on web")
                    query=myCommand()
                url = "http://www.google.de/search?q="+ query
                #speak('Searching the best result on web for you...')
                webbrowser.open(url)
            except:
                speak('Sorry Sir! there is some temporary connection problem at this moment!....\n please try again later')

        
        else:
            try:
                speak("sorry i don't know")
                url = "http://www.google.de/search?q="+ query
                speak('Searching the best result on web for you...')
                webbrowser.open(url)
            except:
                speak("i am really sorry..!!!")
            

        

            
            
            
                
                
                
                
        #speak('Next Command! Sir!')
        








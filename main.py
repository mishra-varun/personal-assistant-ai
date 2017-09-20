
import pyaudio
import speech_recognition as sr
from pygame import mixer
import os
import random
import socket
import webbrowser
import subprocess
import glob
from time import localtime, strftime
import speakmodule

doss = os.getcwd()
i=0
n=0

INFO = '''
        
        +----------------------+
        |Your Virtual Assistant|
        +======================+
        |      OPTIONS:        |
        |#Latest news          |
        |#Stock market view    |
        |#Play music           |
        |#Toggle wi-fi         |
        |#Open up web pages    |
        |#Google maps          |
        |#Install apps         |
        |#Negotiate around your|
        |PC with your voice    |
        '''
print(INFO)
# JARVIS'S EARS======================== SENSITIVE BRAIN
# obtain audio
while (i<1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.adjust_for_ambient_noise(source)
        n=(n+1)     
        print("Say something!")
        audio = r.listen(source)
                                                   # interprete audio (Google Speech Recognition)
    try:
        s = (r.recognize_google(audio))
        message = (s.lower())
        print (message)


# POLITE JARVIS ====== BRAIN 1
    
        if ('goodbye') in message:                          
            rand = ['Goodbye Sir', 'Powering off in 3, 2, 1, 0']
            speakmodule.speak(rand,n,mixer)
            break
            
        if ('hello') in message or ('hi') in message:
            rand = ['Welcome to the virtual intelligence project. At your service sir.']
            speakmodule.speak(rand,n,mixer)

        if ('thanks') in message or ('tanks') in message or ('thank you') in message:
            rand = ['You are wellcome', 'no problem']
            speakmodule.speak(rand,n,mixer)

        if message == ('jarvis'):
            rand = ['Yes Sir?', 'What can I do for you sir?']
            speakmodule.speak(rand,n,mixer)

        if  ('how are you') in message or ('and you') in message or ('are you okay') in message:
            rand = ['Fine thank you']
            speakmodule.speak(rand,n,mixer)

        if  ('*') in message:
            rand = ['Be polite please']
            speakmodule.speak(rand,n,mixer)

        if ('your name') in message:
            rand = ['My name is Jarvis, at your service sir']
            speakmodule.speak(rand,n,mixer)

# USEFUL JARVIS ============ BRAIN 2

        if ('wi-fi') in message:  
            REMOTE_SERVER = "www.google.com"
            speakmodule.wifi()
            rand = ['We are connected']
            speakmodule.speak(rand,n,mixer)

        if ('.com') in message :
            rand = ['Opening' + message]         
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            speakmodule.speak(rand,n,mixer)
            webbrowser.get(Chrome).open('http://www.'+message)
            print ('')
            

        if ('google maps') in message:
            query = message
            stopwords = ['google', 'maps']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")
            rand = [result+'on google maps']
            speakmodule.speak(rand,n,mixer)

        if message != ('start music') and ('start') in message:   
            query = message
            stopwords = ['start']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('start ' + result)
            rand = [('starting '+result)]
            speakmodule.speak(rand,n,mixer)

        if message != ('stop music') and ('stop') in message:
            query = message
            stopwords = ['stop']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('taskkill /im ' + result + '.exe /f')
            rand = [('stopping '+result)]
            speakmodule.speak(rand,n,mixer)

        if ('install') in message:
            query = message
            stopwords = ['install']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            rand = [('installing '+result)]
            speakmodule.speak(rand,n,mixer)
            os.system('python -m pip install ' + result)


        if ('sleep mode') in message:
            rand = ['good night']
            speakmodule.speak(rand,n,mixer)
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        if ('music') in message:
            mus = random.choice(glob.glob(doss + "\\music" + "\\*.mp3"))
            os.system('chown -R user-id:group-id mus')
            os.system('start ' + mus)
            rand = ['start playing']
            speakmodule.speak(rand,n,mixer)

        if ('what time') in message:
            tim = strftime("%X", localtime())
            rand = [tim]
            speakmodule.speak(rand,n,mixer)

    # exceptions
    except sr.UnknownValueError:
        print("$could not understand audio")
    except sr.RequestError as e:
        print("Could not request results$; {0}".format(e))

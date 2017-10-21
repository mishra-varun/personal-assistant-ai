from gtts import gTTS
import random
import os

def speak(rand,n,mixer):
    tts = gTTS(text=random.choice(rand), lang='en')                 
    tts.save('jarvis'+str(n)+'.mp3')
    mixer.init()
    mixer.music.load('jarvis'+str(n)+'.mp3')
    mixer.music.play()

def wifi():
    REMOTE_SERVER = "www.google.com"
    def is_connected():
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 80), 2)
            return True
        except:
            pass
<<<<<<< HEAD
        return False
=======
        return False
>>>>>>> fa766b9927405c3c73aee47bdd78e18adc467516

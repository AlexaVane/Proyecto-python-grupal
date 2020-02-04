#pip install gTTS
#gtts-cli --all
#pip install pipwin
#pipwin install pyaudio
from gtts import gTTS
import sys
from PyQt5 import QtCore, QtGui


tts = gTTS('Hola mundo.', lang='es-us')

with open("hola_mundo.wav", "wb") as archivo:
   tts.write_to_fp(archivo)
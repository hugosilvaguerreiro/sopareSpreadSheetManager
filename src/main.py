import sys
sys.path.insert(0, './input')
sys.path.insert(0, './output')
sys.path.insert(0, './plugins')
sys.path.insert(0, '../libraries/pyttsx-1.0/pyttsx')
import speech_recognition as sr
from Linus import *
from BasicOutput import *
from VoiceOutput import *
from RawInput import *
from MimicPlugin import *
from MicrophoneInput import *
import pyttsx


#linusInputMethod = RawInput()
linusInputMethod = MicrophoneInput()
#linusOutputMethod = BasicOutput()
linusOutputMethod = VoiceOutput()
linusPlugins = [MimicPlugin()]
linus = Linus(linusInputMethod, linusOutputMethod, linusPlugins)

linus.loop()




	
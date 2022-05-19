import pyttsx3 as p
from pyttsx3 import engine

salva=p.init()
voices=salva.getProperty("voices")
salva.setProperty("voice",voices[1].id)
salva.setProperty("rate",120)

salva.say("""
    Batch Operating System
Multiprogramming Operating System
Time-Sharing OS
Multiprocessing OS
Distributed OS
Network OS
Real Time OS
Embedded OS 

 """)

salva.runAndWait()
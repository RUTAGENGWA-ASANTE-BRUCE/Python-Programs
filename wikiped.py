import pyttsx3 as p
from pyttsx3 import engine
import wikipedia
salva=p.init()
voices=salva.getProperty("voices")
salva.setProperty("voice",voices[1].id)
salva.setProperty("rate",120)

def talk(query):
    salva.say(f"""
              
              {query}""")
    
name=input("tell us whom you want information about: ")
info=wikipedia.summary(name)
my_list=info.split(".")
value=0
while True:
    talk(my_list[value])
    print(my_list[value])
    value+=1
    salva.runAndWait()
    continue

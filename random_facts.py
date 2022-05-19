import pyttsx3 as p
from pyttsx3 import engine
import randfacts
engine=p.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",120)

def speak(fact):
    engine.say(f"{fact}")
    engine.runAndWait()
engine.say("Hello motherfucker,  I am gonna kick your ass with some random facts")
fact_number=0
while fact_number<20:
    fact_number+=1
    x=randfacts.get_fact()
    speak(str(fact_number)+", "+x)
    print(str(fact_number)+", "+x)
    continue

   
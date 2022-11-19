import pyttsx3
import datetime
import random

# ---------- Engine Creation --------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 145)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning,sir")
    elif 12 <= hour < 18:
        speak("Good afternoon,sir")
    else:
        speak("Good evening,sir")

    strTime = datetime.datetime.now().strftime("%I:%m %p")
    speak("currently its " + strTime)
    speak("i am friday, online and ready")
    speak("How can i help you?")


def initiate():
    speak("initiating sequence...")
    speak("Starting all system applications,")
    speak("installing and checking all drivers,")
    speak("calibrating and examining all the core processors,")
    speak("Checking internet connection,")
    speak("wait a movement sir,")
    speak("all drivers are up and running, System initiated successfully!,")


def sad():
    try:
        speak("I am sorry to hear that ..., and I hope you feel better soon..., Till that time, tell me what can i do "
              "to cheer you up ?")
    except Exception as error:
        print(error)


def happy():
    try:
        speak("CHEERS!! i am glad to hear that you finally got over your trauma.")
    except Exception as error:
        print(error)

def mapVoice():
    speak("Okay checking !")
    speak("Currently theres some issue finding your exact location, but i am showing your approx location.")

def mood():
    try:
        data = {1: "i am really happy right now!! that i feel like dancing with you.", 2: "i don't know why, but i am not feeling good right now.", 3: "just to be frank, i am quite jealous of you.", 4: "huh!, i don't know but i am feeling broken", 5: "Why are you even asking, as you don't even care about that." }
        num = random.randint(1, 5)
        entry = data[num]
        speak(entry)
    except Exception as error:
        print(error)


def errorcode():
    speak("i am not sure about that ..")


def greeting():
    try:
        lang = {1: "Namaskar", 2: "Hello", 3: "suprabhat", 4: "Hey", 5: "Hi There"}
        num = random.randint(1, 5)
        word = lang[num]
        speak(word)
        print(word)
    except Exception as error:
        print(error)





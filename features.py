import pyttsx3
import wikipedia
import pywhatkit
import datetime
import requests
from bs4 import BeautifulSoup
from GoogleNews import GoogleNews
import wolframalpha
from playsound import playsound
import random


# ---------- Engine Creation --------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 145)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# ----------Google News----------------->
googlenews = GoogleNews()
googlenews = GoogleNews(period='7d')
googlenews.search('india')
result = googlenews.result()


def newsSound():
    try:
        print("playing sound-effect")
        playsound('news.wav')
    except Exception as error:
        print(error)


def coinSound():
    try:
        print("playing sound-effect")
        playsound('coin.wav')
    except Exception as error:
        print(error)


def lostSound():
    try:
        print("playing sound-effect")
        playsound('roll.wav')
    except Exception as error:
        print(error)


def wiki(term):
    try:
        query = term.replace("friday", "")
        query = query.replace("wiki", "")
        speak('Searching Wikipedia...')
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        speak(results)
    except Exception as error:
        print(error)


def playonyt(term):
    try:
        query = term.replace("friday", "")
        query = query.replace("play", "")
        speak("playing " + query + " on youtube music")
        pywhatkit.playonyt(query)
    except Exception as error:
        print(error)


def whois(term):
    try:
        query = term.replace("friday", "")
        query = query.replace("who is", "")
        speak('Searching Wikipedia...')
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        speak(results)
    except Exception as error:
        print(error)


def time():
    try:
        strTime = datetime.datetime.now().strftime("%I:%m %p")
        speak(f"Sir, currently its {strTime}, have a good day!")
    except Exception as error:
        print(error)


def easter01():
    try:
        speak(
            "I am Friday, designed by a group of college students as a final year project.")
        speak("My name stands for, Female Replacement Intelligent Digital Assistant Youth")
        speak("My speciality is, i can better understand human emotions and work on it")
    except Exception as error:
        print(error)


def location():
    try:
        speak("let me check sir,")
        speak("currently there's some issue in finding your exact location,")
        speak("but for reference, we are currently in Narhe area of Pune,Maharashtra")
    except Exception as error:
        print(error)


def temperature(term):
    try:
        search = "temperature in pune"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak(f"currently {search} is {temp}")
    except Exception as error:
        print(error)


def write(term):
    try:
        rememberMsg = term.replace("remember that", "")
        rememberMsg = rememberMsg.replace("friday", "")
        speak("you told me to remember that " + rememberMsg)
        speak("message remembered successfully")
        remember = open('remainders.txt', 'w')
        remember.write(rememberMsg)
        remember.close()
    except Exception as error:
        print(error)


def read():
    try:
        with open('remainders.txt') as text:
            remember = text.read()
        speak("you told me that " + remember)
        text.close()
    except Exception as error:
        print(error)


def news():
    try:
        for x in result:
            print("-" * 50)
            print("title-- ", x['title'])
            speak(x['title'])
            print("description-- ", x['desc'])
            speak(x['desc'])
            print("link-- ", x['link'])
    except Exception as error:
        print(error)


def highlights():
    try:
        for x in result:
            print("-" * 50)
            print("title-- ", x['title'])
            speak(x['title'])

        speak("and, that's it for now, wish you a good day!!")
    except Exception as error:
        print(error)


def weather(term):
    try:
        query = term.replace("what is the weather in", "")
        query = query.replace("what's the weather in", "")
        complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={query}&APPID=68e9ba32e9be4817247cf6974f6f5a9e"

        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temp = y["temp"] - 273.15  # for converting Kelvin to celsius
            current_press = y["pressure"]
            current_humidity = y["humidity"]

            z = x["weather"]
            weather_description = z[0]["description"]
            speak(f"currently in {query} :")

            print("temp = " + str(int(current_temp)) + " degree celsius")
            speak("temp = " + str(int(current_temp)) + " degree celsius")
            print("Atmospheric pressure = " + str(current_press) + " hPa")
            speak("Atmospheric pressure = " + str(current_press) + " hPa")
            print("Humidity = " + str(current_humidity))
            speak("Humidity = " + str(current_humidity))
            print("description = " + str(weather_description))
            speak("description = " + str(weather_description))
        else:
            print("city not found")
            speak("city not found! please try again")
    except Exception as error:
        print(error)


def Wolfram(query):
    api_key = '8X354H-5EJ83W85LG'
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer

    except:
        print("sorry i didn't get that..")
        speak("sorry i didn't get that..")


def calculator(query):

    Term = str(query)
    Term = Term.replace("friday", "")
    Term = Term.replace("calculate", "")
    Term = Term.replace("plus", "+")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("minus", "-")
    Term = Term.replace("into", "*")
    Term = Term.replace("divide by", "/")
    Term = Term.replace("by", "/")

    final = str(Term)

    try:
        result = Wolfram(final)
        print(f"the answer is {result}")
        speak(f"the answer is {result}")
    except:
        print("sorry i didn't get that..")
        speak("sorry i didn't get that..")


def breaker():
    speak('you are welcome sir, always at your command')


def flip():
    try:
        coin = {1: "and, it's a head.", 2: "that's a tail.", 3: "oops!, sorry but i lost the coin, haha"}
        face = random.randint(1, 3)
        chance = coin[face]
        if face == 3:
            lostSound()
            speak(chance)
        else:
            speak(chance)
    except Exception as error:
        print(error)

import sys

import pyttsx3
import speech_recognition as sr
from emotions import wishMe, initiate, sad, happy, mood, mapVoice, errorcode
from features import wiki, playonyt, whois, time, easter01, location, temperature, write, read, news, highlights, \
    weather, calculator, breaker, newsSound, coinSound, flip
from mapmaker import myMap
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from friday_ui import Ui_FridayGUI


# ---------- Engine Creation --------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 145)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.taskExecution()

    # ---------- Input Command -----------------
    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            # query = "hey what's up"
            print(f"user said: {query}\n")

        except Exception as e:
            print(e)
            speak("i didn't get that sir...")
            return "none"

        return query

    def taskExecution(self):
        initiate()
        wishMe()
        while True:

            self.query = self.takeCommand().lower()
            query = self.query.replace("none", "")

            if "wiki" in query:
                wiki(query)

            if "who is" in query:
                whois(query)

            if "play" in query:
                playonyt(query)

            if "time" in query:
                time()

            if "who are you" in query:
                easter01()

            if "location" in query:
                location()

            if "temperature" in query:
                temperature(query)

            if "remember that" in query:
                write(query)

            if "what do you remember" in query:
                read()

            if "news" in query:
                newsSound()
                news()

            if "highlights" in query:
                newsSound()
                highlights()

            if "weather" in query:
                weather(query)

            if "calculate" in query:
                calculator(query)

            if "thanks" in query:
                breaker()

            if "sad" in query:
                sad()

            if "how are you" in query:
                mood()

            if "flip a coin" in query:
                coinSound()
                flip()

            if "map" in query:
                mapVoice()
                myMap()

            else:
                # print("Error: A34")
                error = 1

        if error == 1:
            errorcode()
            error = 0


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_FridayGUI()
        self.ui.setupUi(self)
        self.ui.start.clicked.connect(self.startTask)
        self.ui.end.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("friday_UI/only_ball.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("friday_UI/UI_02.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("friday_UI/UI_03.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("friday_UI/graphs.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("friday_UI/text.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("friday_UI/location2.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()


app = QApplication(sys.argv)
friday = Main()
friday.show()
exit(app.exec_())


import speech_recognition as sr
import pyttsx3
import re

minVoiceIterations = 5
questions = [("how"), ("what"), ("when"), ("where"), ("is"), ("play"), ("open")]


class AccessData:
    def getdata(self):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 50)
        engine.setProperty('voice', voices[1].id)
        engine.say("Hello, I am Athena. How can i help you?")
        engine.runAndWait()

        recog = sr.Recognizer()
        with sr.Microphone() as source:
            i = 0
            while i < minVoiceIterations:
                print("Listening")
                recog.adjust_for_ambient_noise(source)
                audio = recog.listen(source, timeout=10)

                try:
                    print("Voice Recognized")
                    return recog.recognize_google(audio)
                except sr.UnknownValueError:
                    print("Could you please repeat.")
                    i += 1
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
                    i += 1

    def processdata(self, inputstring):
        temp = re.split(r"(\b[\w']+\b)(?:.+|$)", inputstring)[1]
        temp.lower()
        for i in questions:
            if i == temp:
                return questions.index(i)

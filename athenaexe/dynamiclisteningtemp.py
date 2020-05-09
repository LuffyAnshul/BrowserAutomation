import speech_recognition as sr

trigger = "athena"
recog = sr.Recognizer()


def listen():
    print("Beginning to listen...")
    with sr.Microphone() as source:
        recog.energy_threshold = 700
        audio = recog.listen(source, timeout=4)
        try:
            return recog.recognize_google(audio)
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""


while 1:
    if listen().lower() in trigger:
        print("HI")
        break
    else:
        listen()

print("OUT")
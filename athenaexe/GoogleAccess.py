import speech_recognition as sr
import pyttsx3
from selenium import webdriver
from pynput.keyboard import Key, Controller
import time
import re
import string

trigger = "alex"
keyboard = Controller()
minVoiceIterations = 5
decide = [("open new tab"),
          ("close tab"),
          ("search"),
          ("next tab"),
          ("previous tab"),
          ("reopen closed tab"),
          ("select"),
          ("scroll up"),
          ("scroll down"),
          ("refresh"),
          ("full screen"),]
url1 = 'https://www.google.com/search?q='


class GoogleSearch:

    browser = webdriver.Chrome("D:\\MyProjects\\PycharmProjects\\Athena\\athenaexe\\webauto\\chromedriver_win32\\chromedriver.exe")
    max_open = 0
    current_open = 0

    def searchinit(self, input_text):
        self.browser.get(url1 + input_text)

    def decidenext(self):
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
        for i in decide:
            if i in inputstring:
                return decide.index(i)

    def opennewtab(self):
        print("Successfull")
        with keyboard.pressed(Key.ctrl):
            keyboard.press('t')
            keyboard.release('t')
        self.max_open += 1
        self.current_open = self.max_open
        time.sleep(0.1)
        self.browser.switch_to.window(self.browser.window_handles[-1])
    # opentab completed

    def closetab(self):
        with keyboard.pressed(Key.ctrl):
            keyboard.press('w')
            keyboard.release('w')

        if self.current_open == self.max_open:
            self.max_open -= 1
            self.current_open = self.max_open
        elif self.max_open == 0:
            self.browser.quit()
        else:
            self.max_open -= 1

        self.browser.switch_to.window(self.browser.window_handles[self.current_open])
        print(self.current_open)
    # closetab completed

    def search(self):
        recog = sr.Recognizer()
        find = ""
        try:
            with sr.Microphone() as source:
                print("Listening")
                recog.energy_threshold = 400
                audio = recog.listen(source)
                try:
                    print("Voice Recognized")
                    find = recog.recognize_google(audio)
                except sr.UnknownValueError:
                    print("Could you please repeat.")
            self.browser.get(url1 + find)
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)

        except sr.WaitTimeoutError:
            print("Wait timeout Error")
            return ""
    # search completed

    def nexttab(self):
        with keyboard.pressed(Key.ctrl):
            keyboard.press(Key.page_down)
            keyboard.release(Key.page_down)
        time.sleep(2)
        if self.current_open == self.max_open:
            self.current_open = 0
        else:
            self.current_open = ((self.current_open + self.max_open) % self.max_open) + 1
        self.browser.switch_to.window(self.browser.window_handles[self.current_open])
        print(self.current_open)
    # nexttab completed

    def prevtab(self):
        with keyboard.pressed(Key.ctrl):
            keyboard.press(Key.page_up)
            keyboard.release(Key.page_up)
        time.sleep(2)
        if self.current_open == 0:
            self.current_open = self.max_open
        else:
            self.current_open = (self.current_open + self.max_open - 1) % self.max_open
        self.browser.switch_to.window(self.browser.window_handles[self.current_open])
        print(self.current_open)
    # prevtab completed

    def reopenclosed(self):
        with keyboard.pressed(Key.ctrl):
            with keyboard.pressed(Key.shift):
                keyboard.press('t')
                keyboard.release('t')

        self.max_open += 1
        time.sleep(1.5)
        self.browser.switch_to.window(self.browser.window_handles[-1])
    # check for error

    def scrollup(self):
        time.sleep(0.1)
        keyboard.press(Key.page_up)
        keyboard.release(Key.page_up)

    def scrolldown(self):
        time.sleep(0.1)
        keyboard.press(Key.page_down)
        keyboard.release(Key.page_down)

    def select(self):
        searchpage = self.browser.page_source
        links = []
        href = []
        fndall = re.findall(r"<\s*a.href=[\'\"]?https:\/\/([^\'\" >]+)[^>]*>(.*?)<\s*\/\s*a>", searchpage)

        for i in fndall:
            href.append(i[0])
            links.append(i[1])

        # print(href)
        # print(links)

        recog = sr.Recognizer()

        keywords = ""
        try:
            with sr.Microphone() as source:
                print("Listening")
                # recog.energy_threshold = 400
                audio = recog.listen(source)
                try:
                    print("Voice Recognized")
                    keywords = recog.recognize_google(audio)
                except sr.UnknownValueError:
                    print("Could you please repeat.")

        except sr.WaitTimeoutError:
            print("Wait timeout Error")
        keywords = keywords.lower()
        print(keywords)

        exclude = set(string.punctuation)
        fnd_count = [0] * len(links)
        fnd_list = []
        fnd_split = keywords.split()

        for word in fnd_split:
            fnd_list.append(word)
        z = 0
        for sentence in links:
            sentence = " " + sentence.lower()
            sentence = ''.join(ch for ch in sentence if ch not in exclude)
            print(sentence)
            y = 0

            for word in fnd_list:
                result = sentence.find(word, y)
                if result > 0:
                    y = result + len(word)
                    fnd_count[z] += 1

            fnd_count[z] = fnd_count[z] / len(fnd_list) * 100

            print("Match: ", "%.2f" % fnd_count[z], "%")
            z += 1

        prob, index = max([(v, i) for i, v in enumerate(fnd_count)])
        self.browser.get("http://" + href[index])

    def refresh(self):
        self.browser.refresh()

    def fullscreen(self):
        self.browser.fullscreen_window()

    def listeningbackground(self):
        print("Beginning to listen...")
        recog = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                recog.energy_threshold = 400
                audio = recog.listen(source, timeout=4)
                try:
                    print(recog.recognize_google(audio))
                    return recog.recognize_google(audio)
                except sr.UnknownValueError:
                    print("Could not understand audio")
                    return ""
                except sr.RequestError:
                    print("Request Error")
                    return ""
        except sr.WaitTimeoutError:
            print("Wait timeout Error")
            return ""


def gmain(input_text):
    obj = GoogleSearch()
    obj.searchinit(input_text)
    decisiontext = ""

    while True:
        while True:
            currentval = obj.listeningbackground()
            if currentval:
                decisiontext = currentval
                break
        # second while ends

        print(decisiontext)
        decisiontext = decisiontext.lower()
        decisionindex = obj.processdata(decisiontext)

        print(decisionindex)
        # switcher = {
        #     0: obj.opennewtab,
        #     1: obj.closetab,
        #     2: obj.search,
        #     3: obj.nexttab,
        #     4: obj.prevtab,
        #     5: obj.reopenclosed,
        #     6: obj.select,
        #     7: obj.scrollup,
        #     8: obj.scrolldown,
        #     9: obj.refresh,
        #     10: obj.fullscreen,
        # }
        # switcher.get(decisionindex, "Hello Try Again")

        if decisionindex == 0:
            obj.opennewtab()
        elif decisionindex == 1:
            obj.closetab()
        elif decisionindex == 2:
            obj.search()
        elif decisionindex == 3:
            obj.nexttab()
        elif decisionindex == 4:
            obj.prevtab()
        elif decisionindex == 5:
            obj.reopenclosed()
        elif decisionindex == 6:
            obj.select()
        elif decisionindex == 7:
            obj.scrollup()
        elif decisionindex == 8:
            obj.scrolldown()
        elif decisionindex == 9:
            obj.refresh()
        elif decisionindex == 10:
            obj.fullscreen()
        else:
            pass


if __name__ == '__main__':
    gmain("hello world")

from selenium import webdriver
from pynput.keyboard import Key, Controller
import time
import re

keyboard = Controller()
url1 = "https://www.google.com/search?q=hello%20world"
# url2 = "https://www.google.com/search?q=hi"
# url3 = "https://www.google.com/search?q=world"
browser = webdriver.Chrome(
        "C:\\Users\\anshu\\PycharmProjects\\Athena\\athenaexe\\webauto\\chromedriver_win32\\chromedriver.exe")

browser.get(url1)
searchpage = browser.page_source
links = []
href = []
fndall = re.findall(r"<\s*a.href=[\'\"]?https:\/\/([^\'\" >]+)[^>]*>(.*?)<\s*\/\s*a>", searchpage)

for i in fndall:
    href.append(i[0])
    links.append(i[1])
    print(i)

# max_open = 0
# current_open = 0
# reopen = []
#
# with keyboard.pressed(Key.ctrl):
#     keyboard.press('t')
#     keyboard.release('t')
# time.sleep(2)
# max_open += 1
# current_open = max_open
# browser.switch_to.window(browser.window_handles[-1])
# browser.get(url2)
#
# with keyboard.pressed(Key.ctrl):
#     keyboard.press('w')
#     keyboard.release('w')
# time.sleep(2)
# reopen.append(current_open)
# print(reopen)
#
# if current_open == max_open:
#     max_open -= 1
#     current_open = max_open
# else:
#     max_open -= 1
#
#
# # with keyboard.pressed(Key.ctrl):
# #     keyboard.press('t')
# #     keyboard.release('t')
# # time.sleep(2)
# # max_open += 1
# # current_open = max_open
# # browser.switch_to.window(browser.window_handles[-1])
# # browser.get(url3)
# #
# with keyboard.pressed(Key.ctrl):
#     keyboard.press('t')
#     keyboard.release('t')
# time.sleep(2)
# max_open += 1
# current_open = max_open
# browser.switch_to.window(browser.window_handles[-1])
# browser.get(url3)
#
# with keyboard.pressed(Key.ctrl):
#     keyboard.press(Key.page_up)
#     keyboard.release(Key.page_up)
# time.sleep(2)
# if current_open == 0:
#     current_open = ((current_open + max_open - 1) % max_open) + 1
# else:
#     current_open = ((current_open + max_open - 1) % max_open)
# browser.switch_to.window(browser.window_handles[current_open])
# browser.get(url2)
#
# with keyboard.pressed(Key.ctrl):
#     with keyboard.pressed(Key.shift):
#         keyboard.press('t')
#         keyboard.release('t')
#
# max_open += 1
#
# time.sleep(2)
# browser.switch_to.window(browser.window_handles[-1])
# reopen.pop()
# print(reopen)
# time.sleep(1)
# browser.get(url1)
#
#
# # with keyboard.pressed(Key.ctrl):
# #     keyboard.press(Key.page_down)
# #     keyboard.release(Key.page_down)
# # time.sleep(2)
# # if current_open == max_open:
# #     current_open = (current_open + max_open) % max_open
# # else:
# #     current_open = ((current_open + max_open) % max_open) + 1
# # browser.switch_to.window(browser.window_handles[current_open])
# # browser.get(url2)
#
#
#

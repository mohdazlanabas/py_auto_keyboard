from pynput.keyboard import Controller
import time
keyboard = Controller()
time.sleep(5)

content = open('/users/admin//desktop/Python/codePractice/data.txt', "r")
text = content.read()

for char in text:
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.01)
    
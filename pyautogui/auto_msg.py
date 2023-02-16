import pyautogui as gui
import time

msg = input('Enter Your MSG : ')
num = input('Enter Your NUMBER : ')
time.sleep(2)

for i in range(int(num)):
    gui.typewrite(msg)
    gui.press('Enter')

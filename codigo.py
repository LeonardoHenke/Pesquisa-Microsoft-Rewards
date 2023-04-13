import pyautogui 
from time import sleep

x, y = 557, 125
for i in range (0, 34):
    pyautogui.click(x, y, duration=0.3)
    pyautogui.write('a')
    pyautogui.press('enter')
    sleep(1)

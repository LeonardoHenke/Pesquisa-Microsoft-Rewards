import pyautogui
from time import sleep

letras = 'askdjalskjdkasjdlkajskljfrhhbcamzjznhcasdasdfasdfasdfagdafgazxcbfghaseasdba'

cont = 0

x = 557

y = 155 ### Desktop
y = 200 ### Mobile

for i in letras:
    pyautogui.click(x, y, duration=0.3)
    pyautogui.write(i)
    pyautogui.press('enter')
    cont += 1
    if y == 155 and cont == 34:
        break
    elif y == 200 and cont == 24:
        break
    sleep(1.2)

import pyautogui
from time import sleep

letras = 'askdjalskjdkasjdlkajskljfrhhbcamzjznhcasdasdfasdfasdfagdafgazxcbfghaseasdba'

cont = 0

x, y = 557, 155
for i in letras:
    pyautogui.click(x, y, duration=0.3)
    pyautogui.write(i)
    pyautogui.press('enter')
    cont += 1
    if cont == 34:
        break
    sleep(1.2)


# x, y = 557, 200
# for i in letras:
#     pyautogui.click(x, y, duration=0.3)
#     pyautogui.write(i)
#     pyautogui.press('enter')
#     cont += 1
#     if cont == 20:
#         break
#     sleep(1.2)


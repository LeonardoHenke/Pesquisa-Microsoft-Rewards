import pyautogui
from time import sleep

letras = 'askdjalskjdkasjdlkajskljfrhhbcamzjznhcasdasdfasdfasdfagdafgazxcbfghaseasdba'

cont = 0

# x, y = 557, 140
# for i in range (0, 34):
#     for i in letras:
#         pyautogui.click(x, y, duration=0.3)
#         pyautogui.write(i)
#         pyautogui.press('enter')
#         sleep(2)


x, y = 557, 190
for i in letras:
    pyautogui.click(x, y, duration=0.3)
    pyautogui.write(i)
    pyautogui.press('enter')
    cont += 1
    if cont == 22:
        break
    sleep(1)


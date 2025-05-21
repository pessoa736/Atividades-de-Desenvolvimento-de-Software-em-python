import pyautogui
import time
pyautogui.PAUSE = 0.3

repeticoes = 100

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(8)
pyautogui.click(x=476, y=69)

pyautogui.write("https://www.youtube.com/watch?v=hMzu6VM4M8Q")
pyautogui.press("enter")


time.sleep(8)
for i in range(repeticoes):
    pyautogui.click(x=388, y=666)
    pyautogui.write("skibidi "+str(i))
    pyautogui.click(x=472, y=701)
   

    time.sleep(5)
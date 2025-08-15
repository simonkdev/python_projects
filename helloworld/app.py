import pyautogui
import time

pyautogui.moveTo(200,200)

    
pyautogui.keyDown("win")
pyautogui.keyDown("r")
pyautogui.keyUp("win")
pyautogui.keyUp("r")

pyautogui.press(["c", "m", "d", "enter"])

time.sleep(100)

pyautogui.press(["c", "o", "l", "o", "r", "space", "a", "enter"])
pyautogui.press(["d", "i", "r", "/", "a", "enter"])



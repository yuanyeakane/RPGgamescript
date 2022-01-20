import pyautogui
import time
time.sleep(3)
region = (0,0,1920,1080)
im =pyautogui.screenshot(region=region)
#im.save('first.png')
while(1):
    pyautogui.click(1096,230)
    pyautogui.click(1096, 230)
    time.sleep(1)
    pyautogui.click(1414,873)
    pyautogui.click(1414, 873)
    time.sleep(1)
    pyautogui.keyDown('2')
    pyautogui.keyUp('2')
    time.sleep(1)
    pyautogui.keyDown('w')
    pyautogui.keyUp('w')
    time.sleep(5)


import pyautogui
import time
import random
time.sleep(3)
region = (0, 0, 1920, 1080)
im = pyautogui.screenshot(region=region)
# im.save('first.png')
for i in range(1,10000):

    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    pyautogui.keyDown('e')
    pyautogui.keyUp('e')
    time.sleep(1)
    pyautogui.keyDown('2')
    pyautogui.keyUp('2')
    pyautogui.keyDown('q')
    pyautogui.keyUp('q')
    pyautogui.click(960+random.uniform(-600,600), 540+random.uniform(-400,100))
    pyautogui.keyDown('w')
    pyautogui.keyUp('w')
    time.sleep(10)


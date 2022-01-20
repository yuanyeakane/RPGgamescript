import pyautogui
import time
time.sleep(5)
region = (328,36,1264,952)
region_2=(867,230,197,160)
for i in range(1,100000):
    time.sleep(0.1)
    im = pyautogui.screenshot(region=region)
    im.save('jietu/big'+str(i)+'.png')
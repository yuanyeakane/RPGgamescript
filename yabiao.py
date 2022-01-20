
import cv2
import pyautogui
import win32gui, win32con
import os
import time
from matplotlib import pyplot as plt

def imgAutoCick(tempFile):
    time.sleep(1)
    pyautogui.press('space')
    pyautogui.press('space')
    pyautogui.screenshot('big.png',region= (328,36,1264,952))
    im3 = cv2.imread("big.png",1)
    gray = cv2.imread("big.png",0)
    img_template = cv2.imread(tempFile,0)
    w, h = img_template.shape[::-1]
    res = cv2.matchTemplate(gray,img_template,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top = max_loc[0]
    left = max_loc[1]
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(im3, top_left, bottom_right, (0, 0, 255), 2)
    plt.axis('off')  # 关闭坐标
    img3 = cv2.cvtColor(im3, cv2.COLOR_BGR2RGB)  # 颜色转换
    plt.subplot(122), plt.imshow(img3)
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(cv2.TM_CCOEFF_NORMED)
    plt.show()
    time.sleep(0.2)
    pyautogui.moveTo(328+top+h/2, left+w/2)
    pyautogui.rightClick(328+top+h/2, left+w/2)
    pyautogui.rightClick(328+top + h / 2, left + w / 2)

    os.remove("big.png")
if __name__=="__main__":
    # 将代码窗口最小化
    Minimize = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
    time.sleep(3)
    while(1):
        pyautogui.click(1542, 821)
        time.sleep(1)
        pyautogui.click(1409, 813)
        pyautogui.click(1409, 813)
        time.sleep(7)
        pyautogui.click(439, 911)
        pyautogui.click(439, 911)
        time.sleep(1)
        pyautogui.rightClick(951, 335)
        pyautogui.rightClick(951, 335)
        time.sleep(1)
        pyautogui.click(747, 174)
        time.sleep(10)
        pyautogui.click(1477, 945)
        pyautogui.click(1477, 945)
        time.sleep(1)
        pyautogui.press('space')
        time.sleep(1)
        pyautogui.rightClick(760, 300)
        pyautogui.rightClick(760, 300)
        pyautogui.rightClick(760, 300)
        time.sleep(260)





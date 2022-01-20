# 导入模块 cv2匹配算法 plt 显示图片
import cv2
from matplotlib import pyplot as plt

# 读入图片 big1.png是背景大图; small.png是需要寻找的小图（格式.jpg .png都行）
img = cv2.imread("big1.png",0) # 0 读入灰度图
img3 = cv2.imread("big1.png",1) # 1 读入彩色图
img2 = img.copy()
template = cv2.imread("small_2.png",0)
w, h = template.shape[::-1]
img = img2.copy()

# 应用模板算法，返回一系列指标
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) # 从res中挑选最优指标
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

# 显示图片
cv2.rectangle(img3,top_left, bottom_right, (0,0,255), 2) # 画出矩形框






plt.axis('off') # 关闭坐标
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB) # 颜色转换
plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img3)
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle(cv2.TM_CCOEFF_NORMED)
plt.show()

import numpy as np
import cv2
import matplotlib.pyplot as plt

img_bgr = cv2.imread('pycharm.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('pycharm-temp.jpg', 0)

# width and high
w, h = template.shape[::-1]

# result
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

threshold = 0.9
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    # draw rectangular
    cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

cv2.imshow('detected', img_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()

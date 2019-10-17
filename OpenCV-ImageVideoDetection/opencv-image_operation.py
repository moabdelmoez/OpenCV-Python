import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('s2-watch.jpg', cv2.IMREAD_COLOR)

#color this pixel with white color
img[55,55] = [255,255,255]
px = img[55,55]

# print(px)

#roi = region of image

#place a rectangle pixels and fill it white
img[200:250, 200:250] = [255,255,255]

#copy piece of the image
watch_face = img[200:300, 250:350]
img[0:100, 0:100] = watch_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
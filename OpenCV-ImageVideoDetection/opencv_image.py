import numpy as np
import cv2
import matplotlib.pyplot as plt

#read the image from the folder and make it grayscale
img = cv2.imread('s2-watch.jpg', cv2.IMREAD_GRAYSCALE)

#show the image in cv2
cv2.imshow('Ticwatch S2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#matplotlib is RGB but OpenCV is BGR

# #show the image in matplotlib
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()

#to save image in the directory
cv2.imwrite('s2-watch-gray.png', img)

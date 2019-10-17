import numpy as np
import cv2
import matplotlib.pyplot as plt

print(cv2.__version__)

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read() #_ means you tell readers of your code, that you don't need this value

    # Laplacian doesn't work with OpenCV v4.0. It works with v3.xx
    # pip install opencv-python==3.4.5.20﻿
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)

    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    # small numbers mean many edges
    edges = cv2.Canny(frame, 50, 50)

    cv2.imshow('original', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('edges', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
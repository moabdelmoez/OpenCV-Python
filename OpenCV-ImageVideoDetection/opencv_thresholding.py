import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('bookpage.jpeg')

retval, threshold = cv2.threshold(img, 200, 255,cv2.THRESH_BINARY)

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

retval2, threshold2 = cv2.threshold(grayscale, 200, 255,cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

retval2, ostu = cv2.threshold(grayscale, 200, 255, cv2.THRESH_BINARY, cv2.THRESH_OTSU)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus', gaus)
cv2.imshow('ostu', ostu)

cv2.waitKey(0)
cv2.destroyAllWindows()
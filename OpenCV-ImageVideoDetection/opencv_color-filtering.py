import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read() #_ means you tell readers of your code, that you don't need this value
    #convert to HSV (hue, saturation, value)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # #No filter
    # lower_red = np.array([0,0,0])
    # upper_red = np.array([255,255,255])

    lower_red = np.array([169, 100, 100])
    upper_red = np.array([189, 255, 255])

    # #Smoothing and blurring to get rid of noise
    # #Morphological transformations to remove white noise
    # #you can convert single color to HSV color
    # dark_red = np.uint8([[12,22,121]])
    # dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)

    #filter the range of color
    #the range will be everything in the mask
    mask = cv2.inRange(hsv, lower_red, upper_red)
    #show the result in that filter
    res = cv2.bitwise_and(frame, frame, mask=mask)

    #Add blurring
    # kernel = np.ones((15,15), np.float32) / 225
    # smoothed = cv2.filter2D(res, -1, kernel)
    #
    # blur = cv2.GaussianBlur(res, (15,15), 0)
    #
    # median = cv2.medianBlur(res, 15)

    # Morphological Transformations, there are so many types. Morphological Dilation and Erosion. The most basic morphological operations
    # are dilation and erosion.
    # Dilation adds pixels to the boundaries of objects in an image, while erosion removes pixels on object boundaries.

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    # Opening (remove noise in the background) and closing (remove nosie in the foreground)
    # to remove the false negative and false positive
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    #cv2.imshow('mask', mask)
    #cv2.imshow('smoothed', smoothed)
    #cv2.imshow('blur', blur)
    #cv2.imshow('median', median)


    #cv2.imshow('erosion', erosion)
    #cv2.imshow('dilation', dilation)

    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
import numpy as np
import cv2
import matplotlib.pyplot as plt

#first webcam in the device, which is the laptop camera
webcam = cv2.VideoCapture(0)

#if you want to load a video file
# webcam = cv2.VideoCapture('output.avi')

#print(webcam.read())

#save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
outfile = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    #return and the frame, get true or false and the frame array as well
    ret , frame = webcam.read()
    #convert the video to gray color
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    outfile.write(frame)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    #press 'q' to quit the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#finish the webcam shop
webcam.release()
outfile.release()
cv2.destroyAllWindows()
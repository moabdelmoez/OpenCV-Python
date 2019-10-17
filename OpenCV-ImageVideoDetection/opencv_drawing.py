import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('s2-watch.jpg', cv2.IMREAD_COLOR)

#draw the line (img, start, end, color, line_width)
cv2.line(img, (0,0), (500,500), (0,255,0), 10)

#draw the rectangular
cv2.rectangle(img, (50,50), (200,200), (0,0,0), 10)

#draw the circle
cv2.circle(img, (100,200), 55,(255,0,0), -1)

#draw polylines
pts = np.array([[10,20], [34,60], [28,1], [50,10]], np.int32)
cv2.polylines(img, [pts], True, (0,0,255), 3)

#write to an image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Mostafa watch', (0,200), font, 2, (0,255,0), 2, cv2.LINE_AA)

cv2.imshow('image', img)
#press any key to quit
cv2.waitKey(0)
cv2.destroyAllWindows()
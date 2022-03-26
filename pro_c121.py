import cv2
import time
import numpy as np

video = cv2.VideoCapture(0)
image = cv2.imread('mypicture.jpg')
while True:
    ret,frame = video.read()
    frame = cv2.resize(frame,(640,480))
    image = cv2.resize(image,(640,480))
    upper_black = np.array([104,153,70])
    lower_black = np.array([30,30,0])
    mask = cv2.inRange(frame,lower_black,upper_black)
    res = cv2.bitwise_and(frame,frame,mask = mask)
    f1 = frame - res
    f1 = np.where(f1 == 0,image,f1)
    cv2.imshow('Pro C121',frame)
    cv2.imshow('mask',f1)
    cv2.waitKey(1)

video.release()
cv2.destroyAllWindows()

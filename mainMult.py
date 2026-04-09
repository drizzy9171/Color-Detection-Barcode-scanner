#multiple object detection based on colour
import cv2

import numpy as np

from util import getLimits



yellow = [0,255,255] # yellow in bgr colorspace
cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerLimit, upperLimit = getLimits(color= yellow)       #importing limits from util.py function
    
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)    #creating a mask for colour detection
   
    
    # contours for multiple objects that appear in a frame
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        area = cv2.contourArea(contour)
        
        if area > 100:  # filtering noise. (500 default, <500 sensitive(smaller boxes), >500 less sensitive(only large boxes))
            x1, y1, w, h = cv2.boundingRect(contour)
            
            frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), [0,255,0], 5) 
        
    cv2.imshow('LiveCam', frame) 
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
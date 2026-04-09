# Single object detection based on colour
import cv2

from util import getLimits

from PIL import Image

yellow = [0,255,255] # yellow in bgr colorspace
cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerLimit, upperLimit = getLimits(color= yellow)       #importing limits from util.py function
    
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)    #creating a mask for colour detection
    
    maskBounding = Image.fromarray(mask)                    # storing pixel info in array form
    
    bbox = maskBounding.getbbox()                           # getting the bounding boxes
    #print(bbox)
    if bbox is not None:                                    # outlining the detected object
        x1, y1, x2, y2 = bbox
        
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), [0, 255, 0], 5)
        
    cv2.imshow('LiveCam', frame) 
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
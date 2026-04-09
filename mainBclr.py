# color detection + barcode/qr scanning 
import os
os.environ['DYLD_LIBRARY_PATH'] = '/opt/homebrew/opt/zbar/lib'

import cv2

import numpy as np

from util import getLimits

from pyzbar.pyzbar import decode


yellow = [0,255,255]

cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerLimit, upperLimit = getLimits(color= yellow)       
    
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)    
   
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        area = cv2.contourArea(contour)
        
        if area > 150:  
            x1, y1, w, h = cv2.boundingRect(contour)
            
            frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), [0,255,0], 5)

    
    detectedCodes = decode(frame)

    for code in detectedCodes:
        
        x, y, w, h = code.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), [0, 255, 0], 5)

        
        data = code.data.decode('utf-8')
        codeType = code.type

        
        cv2.putText(frame, f'{codeType}: {data}', (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.7, [255, 0, 0], 2)
    
    cv2.imshow('LiveCam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
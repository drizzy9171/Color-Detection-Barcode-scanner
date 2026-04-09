# Barcode/QR detection

import os
os.environ['DYLD_LIBRARY_PATH'] = '/opt/homebrew/opt/zbar/lib'

import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Decode all barcodes/QR codes in the frame
    detectedCodes = decode(frame)

    for code in detectedCodes:
        # Get bounding box
        x, y, w, h = code.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), [0, 255, 0], 5)

        # Decode the data
        data = code.data.decode('utf-8')
        codeType = code.type

        # Display data on frame
        cv2.putText(frame, f'{codeType}: {data}', (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, [255, 0, 0], 2)

    cv2.imshow('LiveCam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
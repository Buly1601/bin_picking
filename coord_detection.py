import sys
import cv2
import numpy as np
import time
import imutils
import matplotlib.pyplot as plt
import HSV_filter as hsv
import find_cubes as cubes
import triangulation as tri

# open camera
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# set camera's lense focal length
f = 4.1
# camera field of view in the horizontal plane in degrees
alpha = 90

while(True):

    ret, frame = camera.read()
    (h, w) = frame.shape[:2]
    # break if camera not responding
    if not ret:
        raise Exception("Camera malfunction")

    else:    
        # apply hsv filter
        mask = hsv.add_HSV_filter(frame, 1)

        # result frames after applying hsv_filter mask
        res = cv2.bitwise_and(frame, frame, mask=mask)

        # apply shape recognition
        circles, coords = cubes.find_circles(frame, mask)

        # transform coords to cm

        # show message
        cv2.putText(frame, f"X: {str(round(coords[0], 3))}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (124, 252, 0), 2)
        cv2.putText(frame, f"Y: {str(round(coords[1], 3))}", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (124, 252, 0), 2)

        # show frames
        cv2.imshow("frame", frame)

        # breaking process
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

camera.release()
cv2.destroyAllWindows()
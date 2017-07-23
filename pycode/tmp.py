import pickle
import cv2
import numpy as np
import os
os.system("clear")

cv2.namedWindow("frame", cv2.WINDOW_AUTOSIZE)
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow("frame", frame)

    if cv2.waitKey(33) == 27:
        break

cap.release()
cv2.destroyAllWindows()


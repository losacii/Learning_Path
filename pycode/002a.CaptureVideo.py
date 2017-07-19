import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(33) & 0xff == 27:
        break
cap.release()
cv2.destroyAllWindows()

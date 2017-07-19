import cv2
import time

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
vfileName = "cap_" + time.strftime("%Y-%m-%d-%H%M%S") + ".mp4"

wtr = cv2.VideoWriter(vfileName, fourcc, 20.0, (640,480))

while True:
    ret, frame = cap.read()
    if frame is None:
        print "No image captured."
        continue
    wtr.write(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xff == 27:
        break

cap.release()
wtr.release()
cv2.destroyAllWindows()
print "file saved..."

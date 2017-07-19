import cv2
import time

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
vfileName = "./saveMedia/cap_" + time.strftime("%Y-%m-%d-%H%M%S") + ".mp4"

wtr = cv2.VideoWriter(vfileName, fourcc, 20.0, (640,480))

recordSwitch = False
while True:
    ret, frame = cap.read()
    if frame is None:
        print "No image captured."
        continue

    if recordSwitch:
        wtr.write(frame)
        cv2.circle(frame, (30,30), 15, (0,0,200), -1)

    cv2.imshow('frame', frame)

    key = cv2.waitKey(20) & 0xff

    if key == 27:
        break
    elif key == ord('r'):
        recordSwitch = not recordSwitch
        print "Record Switch:", recordSwitch


cap.release()
wtr.release()
cv2.destroyAllWindows()
print "file saved..."

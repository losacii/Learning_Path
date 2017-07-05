import cv2
import os
import time
import sys
imagePath = "/home/losa/Pictures/c.png"
os.system("clear")

def aline():
    for i in range(8):
        sys.stdout.write('> ' * 5)
        sys.stdout.flush()
        time.sleep(0.066)
        pass
aline()
print '\n\n'
print ("opencv version:" + cv2.__version__).upper().center(80)
print '\n'
aline()

img = cv2.imread(imagePath)
cv2.imshow('img',img)

cv2.waitKey(3500)
print "\n\nimage shape:", img.shape
print "image size", img.size
cv2.destroyAllWindows()



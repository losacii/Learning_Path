import os
import time
import cv2

def main():
    img = cv2.imread("~/Pictures/tmp/f35.png")
    cv2.imshow('img',img)
    cv2.waitKey()

if __name__ == '__main__':
    os.system("clear")
    main()
    print("\n---Press ENTER to continue---")

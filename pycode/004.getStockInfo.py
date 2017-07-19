# -*- coding: utf-8 -*-
import cv2
import numpy as np
import time, datetime
import urllib2
import re

def getStockInfo():
    font = cv2.FONT_HERSHEY_SIMPLEX
    url = 'http://hq.sinajs.cn/list=s_sh000001'
    backgroundImage = cv2.imread("img/background.png")
    infoSwitch = False
    tmSwitch = True

    while True:

        cv2.imshow("backgroundImage", backgroundImage)
        getKey = cv2.waitKey(200) & 0xFF
        if getKey == 27:
            break
        elif getKey == 115:
            infoSwitch = not infoSwitch
        elif getKey == 116:
            tmSwitch = not tmSwitch

        second = datetime.datetime.now().second
        if second % 5 == 0:
            tm = time.strftime("%Y-%m-%d %H : %M : %S")
            backgroundImage = cv2.imread("img/background.png")

            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            value = response.read().split(',')[1]

            txt = "SH INDEX: " + str(value)

            if tmSwitch:
                cv2.putText(backgroundImage,tm, (20,30),font, 0.5, (200,2000,2000), 1)
            if infoSwitch:
                cv2.putText(backgroundImage,txt, (20,50),font, 0.5, (200,2000,2000), 1)

    cv2.destroyAllWindows()
    print "Exit!\n\n"
    time.sleep(0.3)

if __name__ == '__main__':
    getStockInfo()

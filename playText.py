import sys
import os
import random
import time

put = sys.stdout.write

# fp = open("a.txt").read().split("\n#")

def blit(s):
    os.system("clear")
    strlen = len(s)
    interv = 0.1
    for c in s:
        put(c)
        if c.isalnum():
            time.sleep(interv)
            sys.stdout.flush()
    sys.stdout.flush()
        
    timeToWait = 2.5 + 0.04 * (strlen - 32)
    print("\n~~~~~ (time to wait: {:.2f}s) ~~~~~".format(timeToWait))
    time.sleep(timeToWait)

fileDir = "./rem"

def blitDirOnce():

    for root, dirs, files in os.walk(fileDir):
        random.shuffle(files)

        for file in files:
            if file.endswith(".md"):

                fp = open(os.path.join(root, file)) # open file
                tips = fp.read().split("\n#")       # read, split into tips

                random.shuffle(tips)
                for tip in tips:
                    prefix = file.center(len(file) + 2, ' ').center(80, "~") + "\n\n"
                    blit(prefix + tip)

for i in range(99):
    blitDirOnce()




import sys
import time

while True:
    contents = "\n[{}]\n> ".format(time.strftime("%Y-%m-%d %H:%M:%S"),)
    sys.stdout.write(contents)
    x = raw_input()
    if x == "quit":
        print "DONE!"
        break

'''
    sudo apt install ttyrec
    ttyrec <fileName>
    exit

    ttyplay -s 1.6 <fileName>
'''



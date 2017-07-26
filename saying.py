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

    Ctrl_U - delete all before the cursor
    Ctrl_Y - Paste the deleted commands
    Cltl_l -
    Ctrl_c - Abort commands

    Github: ttygif
    https://github.com/icholy/ttygif

'''



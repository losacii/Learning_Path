from myStore import *
cls()

i = 0

while True:
    put(unichr(i))
    time.sleep(0.2)
    sys.stdout.flush()

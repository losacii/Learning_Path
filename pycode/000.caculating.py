from myStore import *                   # every thing in my store ready
cls()                                   # clear screen

start()                                 # start

blit("Hello friends!")                    # end
blit("Computing is fast, we need slow it down one Million times to show it...")         # blit
blit("Mission starts!")             # blit

put('\n\n')
for i in range(200):
    s = int(2000 * math.sin(i+0.1))
    put(str(s).rjust(10), '\a')
    if i % 10 == 9 and i > 0:
        put('\n')
    sys.stdout.flush()
    time.sleep(0.03)

end()                                   # end



import os, sys, random, time, math

def put(*li):
    for i in li:
        sys.stdout.write(str(i))
        sys.stdout.flush()

def blit(s, w=0.16):
    time.sleep(0.8)
    for i in s:
        if i is ' ':
            time.sleep(w)
            put('\a')
        put(i)
        sys.stdout.flush()
    time.sleep(0.6)
    put('\n', '\a')

def start():
    blit("> " * 16, 0.03)
    put('\n')

def end():
    put('\n\n', "> " * 16, '\n')

def cls():
    os.system("clear")

if __name__ == '__main__':
    os.system("clear")
    blit("> " * 16, 0.03)
    blit('Hello World!')
    blit('I love computing!')



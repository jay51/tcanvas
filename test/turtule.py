
from termios import tcgetattr, TCSADRAIN, tcsetattr
import math
import os
import sys, tty, select
from tcanvas import canvas

def read(f=sys.stdin, old_attr=tcgetattr(sys.stdin.fileno()), time=1, chars=1):
    '''
        cooperative io read from stdin/terminal without pressing enter
    '''

    try:
        tty.setraw(f.fileno())
        rlist, o, e = select.select([f], [], [], time)
    finally:
        tcsetattr(f.fileno(), TCSADRAIN, old_attr)

    if sys.stdin in rlist:
        return sys.stdin.read(chars)

    return ''


def main():
    t = canvas.Turutle(0,0)

    # f = sys.stdin
    # old_attr = tcgetattr(f.fileno())

    while True:
        t.clear_canvas()
        t.display()
        t.forward()

        buff = t.read_char()
        if buff == 'f':
            t.forward()
        if buff == 'r':
            t.right()
        if buff == 'l':
            t.left()
        if buff == 'e':
            exit()
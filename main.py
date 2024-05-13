from tcanvas import canvas
from test import draw_face, draw_face2

from termios import tcgetattr, TCSADRAIN, tcsetattr
import math
import os
import sys, tty, select

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

    f = sys.stdin
    old_attr = tcgetattr(f.fileno())

    while True:

        t.display()
        t.forward()
        # t.print_info()

        buff = read(f, old_attr)
        if buff == 'f':
            t.forward()
        if buff == 'r':
            t.right()
        if buff == 'l':
            t.left()
        if buff == 'e':
            exit()







if os.getenv('TEST'):
    pass
    # Example find angel
    #angle = angle_between_points(x1, y1, x2, y2)
    #print("Angle between points:", angle)

    # Example Rotation angle in degrees
    #rotated_x, rotated_y = rotate_matrix(x2, y2, 180)
    # vector = [x2, y2]
    # angle = -45
    # rotated_vector = rotate_vector(vector, angle)

    # print("Original vector:", vector)
    # print("Rotated vector:", rotated_vector)

elif __name__ == '__main__':
    main()

from tcanvas import canvas
from test import draw_face, draw_face2

from termios import tcgetattr, TCSADRAIN, tcsetattr
import math
import os
import sys, tty, select


def main():

    snake = canvas.Snake()
    snake.run()




if os.getenv('TEST'):
    print('-' * 10)
    pass
    print('-' * 10)
elif __name__ == '__main__':
    main()

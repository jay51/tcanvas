from tcanvas import canvas
from test import draw_face
from test import turtule_main
import sys

print(sys.argv)

if sys.argv[1] == 'face':
    c = canvas.Canvas(30,50)
    draw_face(c)

if sys.argv[1] == 'turtule':
    turtule_main()


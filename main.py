from tcanvas import canvas
from test import draw_face, draw_face2



def main():
    c = canvas.Canvas(30,50, None, 'A', 'B')
    draw_face2(c)

    while False:
        move = input('move ex. 1f: ')
        steps = move[0]
        dirct = move[1]

        if dirct == c.UP:
            pass




if __name__ == '__main__':
    main()

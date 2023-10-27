import canvas



def main():
    c = canvas.Canvas(30,20)

    starting_pos = ((c.CANVAS_ROWS * c.CANVAS_COLS) // 2) + 10

    # c.draw_line(5, 3, c.LEFT)
    # c.draw_line(19, 3, c.RIGHT)

    # c.draw_line(5, 3, c.LEFT)
    # c.draw_line(10, 10, c.DOWN)

    c.draw_line(300, 5, c.UP)

    c.draw_canvas()

    while False:
        move = input('move ex. 1f: ')
        steps = move[0]
        dirct = move[1]

        if dirct == c.UP:
            pass




if __name__ == '__main__':
    main()

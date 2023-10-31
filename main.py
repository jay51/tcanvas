import canvas



def main():
    c = canvas.Canvas(10,20, None, 'A', 'B')

    # canv_mid = (((c.CANVAS_ROWS - 3) * c.CANVAS_COLS) // 2) + 10
    # print(canv_mid)

    # canv_mid = (c.CANVAS_COLS * 3) + (c.CANVAS_COLS // 2)
    # c.set_at_idx(canv_mid, 4, c.LEFT)

    #print((c.CANVAS_COLS // 5) * 3)

    #c.set_row_col(3, 0, 4, c.LEFT)
    # c.set_row_col(3, 10,  7, c.LEFT)

    canv_mid = (c.CANVAS_COLS * 3) + (c.CANVAS_COLS // 2)
    c.set_at_idx(15, 4, c.LEFT)

    # c.draw_line(5, 4, c.DOWN)
    # c.draw_line(5, 4, c.RIGHT)
    # c.draw_line(5, 4, c.UP)

    # c.draw_line(19, 3, c.RIGHT)

    # c.draw_line(5, 3, c.LEFT)
    # c.draw_line(10, 10, c.DOWN)

    # c.draw_line(300, 5, c.UP)

    c.draw_canvas()

    while False:
        move = input('move ex. 1f: ')
        steps = move[0]
        dirct = move[1]

        if dirct == c.UP:
            pass




if __name__ == '__main__':
    main()

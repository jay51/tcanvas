
def draw_face(c):
    # left eye
    row = 3
    canv_mid = (c.CANVAS_COLS * row) + (c.CANVAS_COLS // 5)
    c.set_at_idx(canv_mid, 4, c.LEFT)

    row = (3+1)
    canv_mid = (c.CANVAS_COLS * row) + (c.CANVAS_COLS // 5)
    c.set_at_idx(canv_mid, 3, c.DOWN)

    row = (3+4)
    canv_mid = (c.CANVAS_COLS * row) + (c.CANVAS_COLS // 5)
    c.set_at_idx(canv_mid, 4, c.LEFT)

    row = (3+3)
    canv_mid = (c.CANVAS_COLS * row) + (c.CANVAS_COLS // 5)
    c.set_at_idx(canv_mid-3, 3, c.UP)




    # right eye
    row = 3
    col = 3
    canv_mid = (c.CANVAS_COLS * row) + ((c.CANVAS_COLS//5) * col)
    c.set_at_idx(canv_mid, 4, c.LEFT)

    row = 3+1
    col = 3
    canv_mid = (c.CANVAS_COLS * row) + ((c.CANVAS_COLS//5) * col)
    c.set_at_idx(canv_mid, 3, c.DOWN)

    row = 3+4
    col = 3
    canv_mid = (c.CANVAS_COLS * row) + ((c.CANVAS_COLS//5) * col)
    c.set_at_idx(canv_mid, 4, c.LEFT)

    row = 3+3
    col = 3
    canv_mid = (c.CANVAS_COLS * row) + ((c.CANVAS_COLS//5) * col - 3)
    c.set_at_idx(canv_mid, 3, c.UP)



    # mouth
    row = 15 
    canv_mid = (c.CANVAS_COLS * row) + (c.CANVAS_COLS//3) -2
    c.set_at_idx(canv_mid, 10, c.RIGHT)


    c.draw_canvas()


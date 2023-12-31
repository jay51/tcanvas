
# TODO: import canvas & create inside test function

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



def draw_face2(c):
    # left eye
    c.set_row_col(3, c.CANVAS_COLS//5, 4, c.LEFT)
    c.set_row_col(3+1, c.CANVAS_COLS//5, 3, c.DOWN)
    c.set_row_col(3+4, c.CANVAS_COLS//5, 4, c.LEFT)
    c.set_row_col(3+3, (c.CANVAS_COLS//5)-3, 3, c.UP)

    # right eye
    c.set_row_col(3, (c.CANVAS_COLS//5) * 3, 4, c.LEFT)
    c.set_row_col(3+1, (c.CANVAS_COLS//5) * 3, 3, c.DOWN)
    c.set_row_col(3+4, (c.CANVAS_COLS//5) * 3, 4, c.LEFT)
    c.set_row_col(3+3, ((c.CANVAS_COLS//5) * 3) - 3, 3, c.UP)

    # mouth
    c.set_row_col(15, (c.CANVAS_COLS//3) - 2, 10, c.RIGHT)


    c.draw_canvas()

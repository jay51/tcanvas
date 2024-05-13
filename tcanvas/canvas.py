
import math


class Canvas():

    def __init__(self, rows, cols, canvas=None, symbol='>'):
        self.CANVAS_ROWS = rows # vertical
        self.CANVAS_COLS = cols # horozontal
        self.CANVAS_SIZE = self.CANVAS_ROWS * self.CANVAS_COLS
        # to provid a pre-set canvas
        self.canvas = self.make_canvas() if canvas is None else canvas

        self.symbol = symbol

        self.UP      = 'U'
        self.DOWN    = 'D'
        self.LEFT    = 'L'
        self.RIGHT   = 'R'

    def make_canvas(self) -> [str]:
        return ['.' for c in range(self.CANVAS_ROWS * self.CANVAS_COLS)]

    def set_symbol(self, symbol):
        self.symbol = symbol


    def cls(self):
        print('\x1b[2J\x1b[H', end='')

    def draw_canvas(self):
        for i in range(self.CANVAS_ROWS):
            row_start = i * self.CANVAS_COLS
            # print(row_start)

            row = ' '.join([ self.canvas[c] for c in range(row_start, row_start + self.CANVAS_COLS) ])
            print(row)


    def set_xy(self, x, y, steps, dirct):
        # this method is deprecated
        self.set_row_col(y, x , steps, dirct)
        # self.set_cell(x, y)

    def set_row_col(self, row, col, steps, dirct):
        #       Row(find row) + col
        pos = (row * self.CANVAS_COLS) + col
        self.set_at_idx(pos, steps, dirct)


    def set_at_idx(self, starting_pos: int, steps: int, dirct: str) -> None:
        # this function is deprecated
        if dirct == self.LEFT:
            for i in range(steps):
                # stop from drawing on next row
                row_n = starting_pos // self.CANVAS_ROWS
                left_most = (row_n * self.CANVAS_COLS)

                self.canvas[starting_pos - i] = self.symbol


        elif dirct == self.RIGHT:
            for i in range(steps):
                # stop from drawing on next row
                row_n = starting_pos // self.CANVAS_ROWS
                rigth_most = (row_n * self.CANVAS_COLS) + self.CANVAS_COLS

                self.canvas[starting_pos + i] = self.symbol

        elif dirct == self.UP:
            for i in range(steps):
                idx = starting_pos - (i * self.CANVAS_COLS) if  starting_pos - (i * self.CANVAS_COLS) > 0 else starting_pos

                self.canvas[idx] = self.symbol


        elif dirct == self.DOWN:
            for i in range(steps):
                idx = starting_pos + (i * self.CANVAS_COLS) if  starting_pos + (i * self.CANVAS_COLS) < self.CANVAS_SIZE else starting_pos
                self.canvas[idx] = self.symbol

    def set_cell(self, x, y, symbol=None):
        #       Row(find row) + col
        pos = (y * self.CANVAS_COLS) + x
        row_n = pos // self.CANVAS_ROWS
        rigth_most = (row_n * self.CANVAS_COLS) + self.CANVAS_COLS
        self.canvas[pos] = self.symbol



    def print_info(self):
        print(f'{self.CANVAS_SIZE=}')
        print(f'{self.CANVAS_COLS=}')
        print(f'{self.CANVAS_ROWS=}')




class Turutle:
    def __init__(self, x=0, y=0, canvas=None):
        self.x = x
        self.y = y
        self.angle = 0
        self.canvas = Canvas(30,50) if not canvas else canvas


    def forward(self, steps=1):
        for i in range(steps):
            origin = (self.x, self.y)
            self.x = self.x+1

            self.x, self.y = map(lambda x: round(x), self.rotate_vector((self.x,self.y), self.angle, origin))
            self.canvas.set_cell(self.x, self.y)


    def display(self):
        self.canvas.cls()
        self.canvas.draw_canvas()

    def right(self, angle=45):
        # if the keep doing right, at some point we can go above 360
        # self.angle += angle #this also will work if i just keep it
        if self.angle + angle > 360:
            self.angle = angle
        else:
            self.angle += angle

    def left(self, angle=45):
        # if the keep doing right, at some point we can go below -360
        # self.angle -= angle #this also will work if i just keep it
        if self.angle - angle < -360:
            self.angle = -angle
        else:
            self.angle -= angle


    def rotate_vector(self, vector, angle, center=(0, 0)):
        angle = math.radians(angle)

        x, y = vector
        cx, cy = center
        x -= cx
        y -= cy
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        x_prime = x * cos_theta - y * sin_theta
        y_prime = x * sin_theta + y * cos_theta
        x_prime += cx
        y_prime += cy
        return x_prime, y_prime


    def print_info(self):
        print(f'{self.x=}')
        print(f'{self.y=}')
        print(f'{self.angle=}')

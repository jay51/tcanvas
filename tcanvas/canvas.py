
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

    def clear_canvas(self, default_char=None):
        self.canvas = [default_char if default_char else '.' for c in range(self.CANVAS_ROWS * self.CANVAS_COLS)]

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


    def clear_canvas(self):
        self.canvas.clear_canvas()

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






from termios import tcgetattr, TCSADRAIN, tcsetattr
import math
import time
import os
import sys, tty, select


class Snake():

    def __init__(self, snake_char='D', canvas=None):
        self.length = 0
        self.snake_char = 0
        self.angle = 0
        self.canvas = Canvas(30,50) if not canvas else canvas

        # we need to use the snake as queue where we remove the tial and add new head
        self.snake = [(0,0, snake_char)]


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


    def read(self, f=sys.stdin, old_attr=tcgetattr(sys.stdin.fileno()), time=1, chars=1):
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

    def right(self, angle=45):
        self.angle += angle

    def left(self, angle=45):
        self.angle -= angle


    def remove_tail(self):
        self.snake.pop(0)

    def get_head(self):
        return self.snake[-1]


    def add_new_head(self):
        x, y, _ = self.get_head()
        origin = (x, y)
        x = x + 1

        x, y = map(lambda x: round(x), self.rotate_vector((x,y), self.angle, origin))
        self.snake.append([x, y, self.snake_char])

    def move(self):
        self.add_new_head()
        self.remove_tail()

        for point in self.snake:
            self.canvas.set_cell(point[0], point[1], point[2])

    def run(self):
        f = sys.stdin
        old_attr = tcgetattr(f.fileno())
        previous_time = time.time()

        while True:
            current_time = time.time()
            delta_time = current_time - previous_time

            buff = self.read(f, old_attr, time=1)
            if True: #delta_time >= 1.0:
                self.canvas.cls()
                self.canvas.draw_canvas()

                if buff == 't':
                    self.add_new_head()
                if buff == 'w':
                    self.left()
                    self.left()
                if buff == 's':
                    self.right()
                    self.right()
                if buff == 'd':
                    self.right()
                if buff == 'a':
                    self.left()
                if buff == 'e':
                    exit()

                self.canvas.cls()
                self.canvas.clear_canvas()
                self.move()
                self.canvas.draw_canvas()

                previous_time = current_time


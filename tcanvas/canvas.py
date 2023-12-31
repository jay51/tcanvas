


class Canvas():

    def __init__(self, rows, cols, canvas=None, vert_bar='|', horz_bar='-'):
        self.CANVAS_ROWS = rows # vertical
        self.CANVAS_COLS = cols # horozontal
        self.CANVAS_SIZE = self.CANVAS_ROWS * self.CANVAS_COLS
        # to provid a pre-set canvas
        self.canvas = self.make_canvas() if canvas is None else canvas

        self.vert_bar = vert_bar
        self.horz_bar = horz_bar

        self.UP      = 'U'
        self.DOWN    = 'D'
        self.LEFT    = 'L'
        self.RIGHT   = 'R'

    def make_canvas(self) -> [str]:
        return ['.' for c in range(self.CANVAS_ROWS * self.CANVAS_COLS)]



    def draw_canvas(self):
        for i in range(self.CANVAS_ROWS):
            row_start = i * self.CANVAS_COLS
            # print(row_start)

            row = ' '.join([ self.canvas[c] for c in range(row_start, row_start + self.CANVAS_COLS) ])
            print(row)


    def set_row_col(self, row, col, steps, dirct):
        pos = (row * self.CANVAS_COLS) + col
        self.set_at_idx(pos, steps, dirct)


    def set_at_idx(self, starting_pos: int, steps: int, dirct: str) -> None:
        if dirct == self.LEFT:
            for i in range(steps):
                # stop from drawing on next row
                row_n = starting_pos // self.CANVAS_ROWS
                left_most = (row_n * self.CANVAS_COLS)

                #self.print_info()
                #print(f'row_n: {row_n}')
                #print(f'left_most: {left_most}')
                #print(f'starting_pos: {starting_pos}')

                #if starting_pos - i < left_most:
                    #break

                self.canvas[starting_pos - i] = self.horz_bar


        elif dirct == self.RIGHT:
            for i in range(steps):
                # stop from drawing on next row
                row_n = starting_pos // self.CANVAS_ROWS
                rigth_most = (row_n * self.CANVAS_COLS) + self.CANVAS_COLS

                #if starting_pos + i > rigth_most -1:
                    #break
                
                self.canvas[starting_pos + i] = self.horz_bar

        elif dirct == self.UP:
            for i in range(steps):
                idx = starting_pos - (i * self.CANVAS_COLS) if  starting_pos - (i * self.CANVAS_COLS) > 0 else starting_pos
                # print(f'idx: {idx}')

                self.canvas[idx] = self.vert_bar


        elif dirct == self.DOWN:
            for i in range(steps):
                # idx = (starting_pos + (i * 20)) % CANVAS_SIZE make it wrap
                idx = starting_pos + (i * self.CANVAS_COLS) if  starting_pos + (i * self.CANVAS_COLS) < self.CANVAS_SIZE else starting_pos
                self.canvas[idx] = self.vert_bar



    def print_info(self):
        print(f'{self.CANVAS_SIZE=}')
        print(f'{self.CANVAS_COLS=}')
        print(f'{self.CANVAS_ROWS=}')



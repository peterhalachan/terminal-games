from random import randint
from .app import *
from copy import deepcopy


class Tetris(App):
    def __init__(self):
        super(Tetris, self).__init__()
        self.MAX_ROWS = 10
        self.MAX_COLUMNS = 10

        self.block_types = {
            1: [[0, self.MAX_COLUMNS/2], [-1, self.MAX_COLUMNS/2], [-2, self.MAX_COLUMNS/2], [-3, self.MAX_COLUMNS/2]],
            2: [[0, self.MAX_COLUMNS/2], [0, self.MAX_COLUMNS/2+1], [-1, self.MAX_COLUMNS/2],
                [-1, self.MAX_COLUMNS/2+1]],
            3: [[0, self.MAX_COLUMNS/2-1], [0, self.MAX_COLUMNS/2], [-1, self.MAX_COLUMNS/2],
                [-2, self.MAX_COLUMNS/2]],
            4: [[0, self.MAX_COLUMNS/2-1], [0, self.MAX_COLUMNS/2], [0, self.MAX_COLUMNS/2+1],
                [-1, self.MAX_COLUMNS/2]],
            5: [[0, self.MAX_COLUMNS/2-1], [0, self.MAX_COLUMNS/2], [-1, self.MAX_COLUMNS/2],
                [-1, self.MAX_COLUMNS/2+1]],
        }

        self.blocks = deepcopy(dict.__getitem__(self.block_types, randint(1, len(self.block_types))))
        self.left_border = self.set_left_border()
        self.right_border = self.set_right_border()
        self.in_key = ''

    def array(self):
        board, line = [], []
        for row in range(self.MAX_ROWS):
            for column in range(self.MAX_COLUMNS):
                for coordinates in self.blocks:
                    if row == list.__getitem__(coordinates, 0) and column == list.__getitem__(coordinates, 1):
                        line.append('x')
                try:  # checks if the player was placed, if not places a dot
                    list.__getitem__(line, column)
                except IndexError:
                    line.append('.')
            board.append(line)
            line = []
        return board

    def set_left_border(self):
        min_value = 9
        for i in range(0, 4):
            if self.blocks[i][1] < min_value:
                min_value = self.blocks[i][1]
        return min_value

    def set_right_border(self):
        max_value = 0
        for i in range(0, 4):
            if self.blocks[i][1] > max_value:
                max_value = self.blocks[i][1]
        return max_value

    def new_block(self):
        for k in range(0, 4):
            if self.blocks[k][0] == self.MAX_ROWS - 1:
                return self.get_new_block_type()

            for i in range(4, len(self.blocks)):
                self.blocks[k][0] += 1
                if self.blocks[k] == self.blocks[i]:
                    self.blocks[k][0] -= 1
                    return self.get_new_block_type()
                else:
                    self.blocks[k][0] -= 1

    def get_new_block_type(self):
        upcoming_block = randint(1, len(self.block_types))
        for block in self.block_types[upcoming_block]:
            self.blocks.insert(0, deepcopy(block))
        self.right_border = self.set_right_border()
        self.left_border = self.set_left_border()

    def change_position(self, down, direction):
        if down:
            for i in range(0, 4):
                self.blocks[i][0] += 1
        else:
            for i in range(0, 4, 1):
                self.blocks[i][1] += direction
                self.blocks[i][0] += 1

    def delete_row(self):
        rows = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for block in self.blocks:
            rows[block[0]] += 1
        for row in rows:
            if row >= 9:
                for i in range(0, 10):
                    self.blocks.remove([row, i])

    def control(self, in_key):
        self.in_key = in_key
        if in_key == 's' or in_key == 'S' or in_key == '2' or in_key is None:
            self.change_position(True, 1)  # to each row add 1
        elif self.right_border < self.MAX_COLUMNS-1 and (in_key == 'd' or in_key == 'D' or in_key == '6'):  # to right
            self.change_position(False, 1)  # to each column add 1
            self.right_border += 1
        elif self.left_border > 0 and (in_key == 'a' or in_key == 'A' or in_key == '4'):  # to left
            self.change_position(False, -1)  # each column subtract by 1
            self.left_border -= 1
        elif in_key == 'q':
            raise Stop
        else:
            self.change_position(True, 1)
        self.new_block()

# TODO
# end game when the top is reached
# tests
# multithreading
# blocks fall down after delete
# DONE delete rows
# DONE end of fall when beneath is another block
# DONE blocks go out of area

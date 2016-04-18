from random import randint
from copy import deepcopy
from .app import *


class Snake(App):
    def __init__(self, rows=10, cols=10):
        super(Snake, self).__init__()
        self.player = [[0, 2], [0, 1], [0, 0]]  # row, column
        self.last_part = deepcopy(self.player[len(self.player) - 1])
        self.direction = 'E'  # North, West, East, South -> describes the direction of movement
        self.fruit = [3, 3]
        self.MAX_ROWS = rows
        self.MAX_COLUMNS = cols
        self.MAX_SNAKE_SIZE = self.MAX_COLUMNS * self.MAX_ROWS

        self.in_key = ''

    def array(self):
        board, line = [], []
        for row in range(self.MAX_ROWS):
            for column in range(self.MAX_COLUMNS):
                for player_coordinates in self.player:
                    if row == list.__getitem__(player_coordinates, 0) and \
                                    column == list.__getitem__(player_coordinates, 1):
                        if not (row == self.player[0][0] and column == self.player[0][1]):
                            line.append('O')
                        else:
                            if self.direction == 'E':
                                line.append('>')
                            elif self.direction == 'W':
                                line.append('<')
                            elif self.direction == 'N':
                                line.append('^')
                            else:
                                line.append('V')
                if row == list.__getitem__(self.fruit, 0) and column == list.__getitem__(self.fruit, 1):
                    line.append('X')
                try:  # checks if the player was placed, if not places a dot
                    list.__getitem__(line, column)
                except IndexError:
                    line.append('.')
            board.append(line)
            line = []
        return board

    def new_fruit(self):
        self.fruit[0] = randint(0, self.MAX_ROWS - 1)
        self.fruit[1] = randint(0, self.MAX_COLUMNS - 1)
        for player_coordinates in self.player:
            if list.__getitem__(player_coordinates, 0) == list.__getitem__(self.fruit, 0) and \
                            list.__getitem__(player_coordinates, 1) == list.__getitem__(self.fruit, 1):
                self.new_fruit()
        return self.fruit

    def eat(self, add_part):
        if self.player[0][0] == self.fruit[0] and self.player[0][1] == self.fruit[1]:
            self.player.append([add_part])
            self.new_fruit() if len(self.player) != self.MAX_SNAKE_SIZE else self.end_game(1)

    def swap(self):
        for part_num in range(len(self.player) - 1, 1, -1):
            self.player[part_num] = deepcopy(list.__getitem__(self.player, part_num - 1))
        self.player[1] = deepcopy(list.__getitem__(self.player, 0))

    def just_do_it(self):
        self.last_part = deepcopy(self.player[len(self.player) - 1])
        self.swap()

    def move(self):
        self.just_do_it()
        if self.direction == 'N':
            self.player[0][0] -= 1 if self.player[0][0] > 0 else self.end_game(0)
        elif self.direction == 'S':
            self.player[0][0] += 1 if self.player[0][0] < self.MAX_ROWS-1 else self.end_game(0)
        elif self.direction == 'E':
            self.player[0][1] += 1 if self.player[0][1] < self.MAX_COLUMNS-1 else self.end_game(0)
        else:
            self.player[0][1] -= 1 if self.player[0][1] > 0 else self.end_game(0)
        for i in range(1, len(self.player)):
            if list.__getitem__(self.player, 0) == list.__getitem__(self.player, i):
                self.end_game(0)

        self.eat(self.last_part)

    def control(self, in_key):
        if in_key is not None:
            self.in_key = in_key[0]
        if (in_key == 'w' or in_key == 'W' or in_key == '8') and self.direction != 'S':
            self.direction = 'N'
        elif (in_key == 's' or in_key == 'S' or in_key == '2') and self.direction != 'N':
            self.direction = 'S'
        elif (in_key == 'd' or in_key == 'D' or in_key == '6') and self.direction != 'W':
            self.direction = 'E'
        elif (in_key == 'a' or in_key == 'A' or in_key == '4') and self.direction != 'E':
            self.direction = 'W'
        elif in_key == 'q':
            raise Stop
        else:
            pass

        self.move()
        self.in_key = ''

from __future__ import print_function
import msvcrt  # read pydoc for more info, nice shit
import os
import time


class Stop(Exception):
    pass


class App(object):
    def array(self):
        raise NotImplementedError

    def control(self, in_key):
        raise NotImplementedError

    @staticmethod
    def print_board(board):
        for row in board:
            print(" ".join(row))

    @staticmethod
    def end_game(result):
        for _ in range(0, 3):
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(0.2)
            if result == 0:
                print('You lose!', end='')
            else:
                print('You win!', end='')
            time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        raise Stop


def get_input(timeout=1):  # timed input without echo for Win
    start_time = time.time()
    in_key = ''

    while True:
        if msvcrt.kbhit():
            in_key = msvcrt.getch()
            # in_key += chr
            break
        if len(in_key) == 0 and (time.time() - start_time) > timeout:
            break

    sleep = round((abs(timeout - (time.time() - start_time))), 2)
    if len(in_key) > 0:
        time.sleep(sleep)
        return in_key[0]
    else:
        return None

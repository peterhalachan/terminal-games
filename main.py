from __future__ import print_function
from os import system, name
from sys import exit
from msvcrt import getch
from games.snake import Snake
from games.tetris import Tetris
from games.app import get_input, Stop


def main_menu(selection=0, choice=0):
    system('cls' if name == 'nt' else 'clear')  # cls for WIN

    menu = {
        "1 Select a game": ["1 Snake", "2 Tetris", "2 Back"],
        "2 Options": ["1 Back"],
        "3 Quit": None
    }

    if choice == 0:
        array = sorted(menu.keys())
    elif choice == 1:
        array = menu["1 Select a game"]
    elif choice == 2:
        array = menu["2 Options"]
    else:
        exit(1)

    # printing the menu to the terminal
    for i in range(len(array)):
        if i != selection:
            print(" \t" + array[i][2:])
        else:
            print(">\t" + array[i][2:])

    in_key = getch()
    print(in_key)
    if selection != len(array)-1 and (in_key == "s" or in_key == "S" or in_key == "2"):
        selection += 1
    elif selection != 0 and (in_key == "w" or in_key == "W" or in_key == "8"):
        selection -= 1
    elif ord(in_key) == 13:
        if array[selection][2:] == "Back":
            selection = 0
            choice = 0
        elif choice == 1:
            return game_launcher(selection)
        else:
            choice = selection + 1
            selection = 0
    else:
        pass

    if in_key == 'q':
        exit(1)

    return main_menu(selection, choice)


def game_launcher(val):
    if val == 0:
        game = Snake()
        game.new_fruit()
    elif val == 1:
        game = Tetris()
    while True:
        system('cls' if name == 'nt' else 'clear')  # cls for WIN
        game.print_board(game.array())
        print('\nPress "q" to quit.', end='')
        try:
            game.control(get_input(0.5))
        except Stop:
            break


if __name__ == '__main__':
    main_menu()

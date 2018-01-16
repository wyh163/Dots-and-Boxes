# -*- coding: UTF-8 -*-
from .game import *
from .model import Color
import os


class DotsAndBoxes:
    def __init__(self):
        self._current_game = None
        self._history = None
        self._current_move = None

    def new_game(self):
        self._current_game = Game()
        self._history = []
        self._current_move = 0

    def move(self, input_str):
        if (self._current_game == None):
            raise DBError("Do not have current game")

        color = None
        x = None
        y = None
        mode = None
        try:
            if (input_str[0] == 'r' or input_str[0] == 'R'):
                color = Color.red
            elif (input_str[0] == 'b' or input_str[0] == 'B'):
                color = Color.blue
            else:
                raise ValueError()
            if (input_str[2] == 'a' or input_str[2] == 'A'):
                x = 'a'
            elif (input_str[2] == 'b' or input_str[2] == 'B'):
                x = 'b'
            elif (input_str[2] == 'c' or input_str[2] == 'C'):
                x = 'c'
            elif (input_str[2] == 'd' or input_str[2] == 'D'):
                x = 'd'
            elif (input_str[2] == 'e' or input_str[2] == 'E'):
                x = 'e'
            elif (input_str[2] == 'f' or input_str[2] == 'F'):
                x = 'f'
            else:
                raise ValueError()
            y = int(input_str[3])
            if (y < 0 or y > 6):
                raise ValueError()
            if (input_str[5] == 'v' or input_str[5] == 'V'):
                mode = 'v'
            elif (input_str[5] == 'h' or input_str[5] == 'H'):
                mode = 'h'
            else:
                raise ValueError
        except (IndexError, ValueError, TypeError):
            raise DBError("Invalid input", input_str)

        self._current_game.move(color, (x, str(y), mode))

        self._history.append((color, (x, str(y), mode)))
        self._current_move = self._current_move + 1

    def run(self):
        self._main_menu()
        user_input = 0
        while (not user_input == 4):
            user_input = int(input("Please enter: "))
            if (user_input == 1):
                self.new_game()
                self._play_game()
                break
            if (user_input == 2):
                pass
            if (user_input == 3):
                pass
            self._main_menu()
            user_input = int(input("Input errors, please re-enter: "))

    def _main_menu(self):
        os.system('clear')
        num = int(os.get_terminal_size()[0]/2)-10
        print("="*num + "=== Dots & Boxes ===" + "="*num)
        print(" "*num + "    1 New Game      ")
        print(" "*num + "    2 Load Game     ")
        print(" "*num + "    3 Save Game     ")
        print(" "*num + "    4 Exit          ")
        print("="*num + "====================" + "="*num)

    def _play_game(self):
        os.system('clear')
        print("Game is start.")
        while (not self._current_game.is_end):
            if (self._current_game.current_player == Color.red):
                print("RED: ", end = '')
            else:
                print("BLUE: ", end = '')
            input_str = input()
            self.move(input_str)

        if (self._current_game.winner == Color.red):
            print("Winner is RED!")
        else:
            print("Winner is BLUE!")


class DBError(DBException):
    def __init__(self, *args, **kwargs):
        pass


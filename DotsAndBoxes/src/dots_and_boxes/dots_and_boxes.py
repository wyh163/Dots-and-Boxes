# -*- coding: UTF-8 -*-
from .game import *
from .model import Color
import os


class DotsAndBoxes:
    def __init__(self):
        self._current_game = None
        self._history = None
        self._current_move = None
        self._current_step = None

    @property
    def last_move(self):
        if (self._current_game == None or self._current_step == 0):
            raise DBError("Do not have step")
        return (self._current_step, self._history[self._current_step-1])


    def new_game(self):
        self._current_game = Game()
        self._history = []
        self._current_step = 0

    def move_with_str(self, input_str):
        if (self._current_game == None):
            raise DBError("Do not have current game")

        self.move(self._str_to_piece(input_str))

    def _str_to_piece(self, input_str):
        color = x = y = mode = None
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

        return (color, (x, str(y), mode))

    def move(self, piece):
        color = piece[0]
        coordinate = piece[1]

        self._current_game.move(color, coordinate)

        if (self._current_step < len(self._history)):  # 当从某一历史步直接下新步时 (先行判断可以避免_history越界)
            if (not piece == self._history[self._current_step]):  # 如果新步与历史步的下一步历史不同
                while (self._current_step < len(self._history)):  # 先删除这一历史步之后的数据
                    self._history.pop()
                self._history.append(piece)
        else:
            self._history.append(piece)
        self._current_step = self._current_step + 1

    def back(self):
        if (self._current_game == None):
            raise DBError("Do not have current game")
        if (self._current_step == 0):
            raise DBError("Do not have step")

        self._current_game.back()

        self._current_step = self._current_step - 1

    def turn_to(self, step_num):
        if (step_num < 0 or step_num > len(self._history) or step_num == self._current_step):
            raise DBError("Invalid step num")

        while (self._current_step > step_num):
            self.back()

        while (self._current_step < step_num):
            self.move(self._history[self._current_step])

    def run(self):
        self._main_menu()
        user_input = 0
        while (not user_input == 4):
            user_input = int(input("Please enter: "))
            if (user_input == 1):
                if (self._current_game == None):
                    self.new_game()
                self._play_game()
            if (user_input == 2):
                pass
            if (user_input == 3):
                pass

    def _main_menu(self):
        os.system('clear')
        num = int(os.get_terminal_size()[0]/2)-10
        print("="*num +     "=== Dots & Boxes ===" + "="*num)
        if (self._current_game == None):
            print(" "*num + "    1 New Game      ")
        else:
            print(" "*num + "    1 Continue Game ")
        print(" "*num +     "    2 Load Game     ")
        print(" "*num +     "    3 Save Game     ")
        print(" "*num +     "    4 Exit          ")
        print("="*num +     "====================" + "="*num)

    def _play_game(self):
        os.system('clear')
        print("Game is start.")
        while (not self._current_game.is_end):
            if (self._current_game.current_player == Color.red):
                print("RED: ", end='')
            else:
                print("BLUE: ", end='')
            input_str = input()
            self.move(input_str)

        if (self._current_game.winner == Color.red):
            print("Winner is RED!")
        else:
            print("Winner is BLUE!")


class DBError(DBException):
    def __init__(self, *args, **kwargs):
        pass


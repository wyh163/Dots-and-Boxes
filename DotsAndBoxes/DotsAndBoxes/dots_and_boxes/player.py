# -*- coding: UTF-8 -*-
import threading, time

from .model import *


class Player:
    def __init__(self, color, name):
        self._color = color
        self._name = name
        self._score = 0

    @property
    def color(self):
        return self._color

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    def _start_new_game(self):
        self._score = 0
        self.start_new_game()

    def _game_is_over(self, is_win):
        self.game_is_over(is_win)

    def start_new_game(self):
        pass

    def game_is_over(self, is_win):
        pass


class HumanPlayer(Player):
    def __init__(self, color, name, game_controller):
        super(HumanPlayer, self).__init__(color, name)
        self.__game_controller = game_controller

    def move(self, coordinate):
        self.__game_controller.move(Piece(self.color, coordinate))


class AIPlayer(Player):
    def __init__(self, color, name, game_controller):
        super(AIPlayer, self).__init__(color, name)
        self.__game_controller = game_controller
        self._board = None
        self._history = None
        self._last_piece = None
        self.__thread = None

    def last_move(self, piece, board, history, next_player_color):
        self._board = board
        self._history = history
        self._last_piece = piece
        if (next_player_color == self.color):
            self.__thread = threading.Thread(target=self.move)
            self.__thread.start()

    def move(self, coordinate=None):
        time.sleep(0.01)
        self.__game_controller.move(Piece(self.color, coordinate))

    def start_new_game(self):
        pass

    def game_is_over(self, is_win):
        pass


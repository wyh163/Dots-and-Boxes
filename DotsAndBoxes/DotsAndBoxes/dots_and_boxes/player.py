# -*- coding: UTF-8 -*-
import threading

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
        self._last_piece = None
        self.__thread = None

    def last_move(self, piece, board):
        self._board = board
        self._last_piece = piece
        self.__thread = threading.Thread(target=self.move)
        self.__thread.start()

    def move(self, coordinate=None):
        self.__game_controller.move(Piece(self.color, coordinate))


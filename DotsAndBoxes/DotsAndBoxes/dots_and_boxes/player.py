# -*- coding: UTF-8 -*-
import threading
import random

from .model import *


class Player:
    def __init__(self, color, name, game_controller):
        self._color = color
        self._name = name
        self._score = 0
        self._game_controller = game_controller

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
        super(HumanPlayer, self).__init__(color, name, game_controller)

    def move(self, coordinate):
        self._game_controller.move(Piece(self.color, coordinate))


class AIPlayer(Player):
    def __init__(self, color, name, game_controller):
        super(AIPlayer, self).__init__(color, name, game_controller)
        self._board = None
        self._last_piece = None
        self.__thread = None

    def last_move(self, piece, board):
        self._board = board
        self._last_piece = piece
        # self.__thread = threading.Thread(target=self.move)
        # self.__thread.setDeamon(True)
        # self.__thread.start()
        self.move()

    def move(self):
        while True:
            coordinate = (random.choice("abcdef"), random.choice("123456"), random.choice(["h", "v"]))
            try:
                self._board.set_piece(Piece(self.color, coordinate))
                break
            except (PieceCoordinateError, BoardError) as e:
                continue

        self._game_controller.move(Piece(self.color, coordinate))


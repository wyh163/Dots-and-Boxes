# coding = UTF-8
from .model import *


class Game:
    def __init__(self, red_player, blue_player):
        if not (red_player.color() == Color.red and blue_player.color() == Color.blue):
            raise TypeError("Wrong player type.", red_player, blue_player)
        self._red_player = red_player
        self._blue_player = blue_player

        self.board = Board(self)

    def add_score(self, color):
        if (color == Color.red):
            self._red_player.score = self._red_player.score + 1
        else:
            self._blue_player.score = self._blue_player.score + 1


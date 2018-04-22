# -*- coding: UTF-8 -*-

class Player:
    def __init__(self, color, name, game_controller):
        self._color = color
        self._name = name
        self._score = 0
        self._game_controller = game_controller
        self._is_start = False

    @property
    def color(self):
        return self._color

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    def last_move(self, piece, board):
        pass

    def start(self):
        self._is_start = True


class HumanPlayer(Player):
    def __init__(self, color, name, game_controller):
        super(HumanPlayer, self).__init__(color, name, game_controller)

    def move(self, coordinate):
        self._game_controller.move(self._color, coordinate)


class AIPlayer(Player):
    def __init__(self, color, name, game_controller):
        super(AIPlayer, self).__init__(color, name, game_controller)


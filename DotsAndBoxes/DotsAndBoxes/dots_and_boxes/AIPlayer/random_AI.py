# -*- coding: UTF-8 -*-
import threading, random

from ..player import AIPlayer
from ..model import *


# 这是一个AI示例，使用随机算法
class RandomAI(AIPlayer):
    def __init__(self, color, name, game_controller):
        super(RandomAI, self).__init__(color, name, game_controller)
        # 通过访问属性获取AI玩家颜色
        print(self.color)
        print(self.name)
        print(self.score)
        # 也可以添加自定义属性

    def start_new_game(self):
        # 做一些游戏开始时的初始化工作
        print("Game is start.")

    def game_is_over(self, is_win):
        # 获得比赛结果
        print("You win!" if is_win else "You lose.")

    def last_move(self, piece, board, history, next_player_color):
        # 可以重载此函数以实现自定义的历史局面保留
        # 重载后请不要调用父类，因为这可能造成保存局面信息的属性被覆盖
        # 同时请注意要异步调用self.move()
        # 以下代码为父类的实现
        self._board = board
        self._history = history
        self._last_piece = piece
        if (next_player_color == self.color):
            self.__thread = threading.Thread(target=self.move)
            self.__thread.start()

    def move(self):
        # 通过访问属性获得当前局面
        print(self._board)
        print(self._last_piece)
        # 在这实现你的落子算法
        while True:
            coordinate = (random.choice("abcdef"), random.choice("123456"), random.choice(["h", "v"]))
            try:
                self._board.set_piece(Piece(self.color, coordinate))
                break
            except (PieceCoordinateError, BoardError):
                continue

        # 记得最后调用父类的move方法，否则无法落子
        super(RandomAI, self).move(coordinate)


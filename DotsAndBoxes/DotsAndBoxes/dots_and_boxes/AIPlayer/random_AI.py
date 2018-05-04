# -*- coding: UTF-8 -*-
import random

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


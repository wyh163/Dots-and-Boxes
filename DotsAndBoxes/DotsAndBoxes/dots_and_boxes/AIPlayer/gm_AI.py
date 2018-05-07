# -*- coding: UTF-8 -*-
import random

from ..player import AIPlayer
from ..model import *


# 这是一个AI示例，使用随机算法
class GMAI(AIPlayer):
    def __init__(self, color, name, game_controller):
        super(GMAI, self).__init__(color, name, game_controller)
        self.step_num = 0
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.box = ([], [], [], [])

    def start_new_game(self):
        self.step_num = 0
                    #  0  1  2  3  4  5  6  7  8  9  10
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
                      [0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0],  # 1
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
                      [0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0],  # 3
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
                      [0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0],  # 5
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
                      [0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0],  # 7
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
                      [0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0],  # 9
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 10
        self.box = ([], [], [], [], [])
        for x in (1, 3, 5, 7, 9):
            for y in (1, 3, 5, 7, 9):
                self.box[4].append((x, y))

    def game_is_over(self, is_win):
        print(is_win)

    def last_move(self, piece, board, next_player_color):
        if piece != None:
            self.step_num = self.step_num + 1
            x, y = piece.coordinate
            self.board[x][y] = 1 if piece.color == self.color else -1
            if x % 2 == 0:
                if x + 1 < 10:
                    if self.board[x+1][y] != 0:
                        self.box[self.board[x+1][y]].remove((x+1, y))
                        self.board[x+1][y] = self.board[x+1][y] - 1
                        self.box[self.board[x+1][y]].append((x+1, y))
                if x - 1 > 0:
                    if self.board[x-1][y] != 0:
                        self.box[self.board[x-1][y]].remove((x-1, y))
                        self.board[x-1][y] = self.board[x-1][y] - 1
                        self.box[self.board[x-1][y]].append((x-1, y))
            else:
                if y + 1 < 10:
                    if self.board[x][y+1] != 0:
                        self.box[self.board[x][y+1]].remove((x, y+1))
                        self.board[x][y+1] = self.board[x][y+1] - 1
                        self.box[self.board[x][y+1]].append((x, y+1))
                if y - 1 > 0:
                    if self.board[x][y-1] != 0:
                        self.box[self.board[x][y-1]].remove((x, y-1))
                        self.board[x][y-1] = self.board[x][y-1] - 1
                        self.box[self.board[x][y-1]].append((x, y-1))

        super(GMAI, self).last_move(piece, board, next_player_color)

    def move(self):
        print(self.step_num)
        if self.step_num < 30:
            if len(self.box[1]) > 0:
                x, y = random.choice(self.box[1])
                if self.board[x+1][y] == 0:
                    super(GMAI, self).move(self.coordinate_exchange((x+1, y)))
                    return
                if self.board[x-1][y] == 0:
                    super(GMAI, self).move(self.coordinate_exchange((x-1, y)))
                    return
                if self.board[x][y+1] == 0:
                    super(GMAI, self).move(self.coordinate_exchange((x, y+1)))
                    return
                if self.board[x][y-1] == 0:
                    super(GMAI, self).move(self.coordinate_exchange((x, y-1)))
                    return
        # if self.step_num < 24:
            arr = []
            if len(self.box[4]) > 0:
                for x, y in self.box[4]:
                    if x + 2 < 10:
                        if self.board[x+2][y] != 2:
                            arr.append((x+1, y))
                    else:
                        arr.append((x+1, y))
                    if x - 2 > 0:
                        if self.board[x-2][y] != 2:
                            arr.append((x-1, y))
                    else:
                        arr.append((x-1, y))
                    if y + 2 < 10:
                        if self.board[x][y+2] != 2:
                            arr.append((x, y+1))
                    else:
                        arr.append((x, y+1))
                    if x - 2 > 0:
                        if self.board[x][y-2] != 2:
                            arr.append((x, y-1))
                    else:
                        arr.append((x, y-1))
            elif len(self.box[3]) > 0:
                for x, y in self.box[3]:
                    if self.board[x+1][y] == 0:
                        if x + 2 < 10:
                            if self.board[x+2][y] != 2:
                                arr.append((x+1, y))
                        else:
                            arr.append((x+1, y))
                    if self.board[x-1][y] == 0:
                        if x - 2 > 0:
                            if self.board[x-2][y] != 2:
                                arr.append((x-1, y))
                        else:
                            arr.append((x-1, y))
                    if self.board[x][y+1] == 0:
                        if y + 2 < 10:
                            if self.board[x][y+2] != 2:
                                arr.append((x, y+1))
                        else:
                            arr.append((x, y+1))
                    if self.board[x][y-1] == 0:
                        if y - 2 > 0:
                            if self.board[x][y-2] != 2:
                                arr.append((x, y-1))
                        else:
                            arr.append((x, y-1))
            if len(arr) > 0:
                super(GMAI, self).move(self.coordinate_exchange(random.choice(arr)))
                return
            if len(self.box[3]) > 0:
                x, y = random.choice(self.box[3])
                if self.board[x+1][y] == 0:
                    arr.append((x+1, y))
                if self.board[x-1][y] == 0:
                    arr.append((x-1, y))
                if self.board[x][y+1] == 0:
                    arr.append((x, y+1))
                if self.board[x][y-1] == 0:
                    arr.append((x, y-1))
            if len(arr) > 0:
                super(GMAI, self).move(self.coordinate_exchange(random.choice(arr)))
                return

        # 在这实现你的落子算法
        while True:
            coordinate = (random.choice("abcdef"), random.choice("123456"), random.choice(["h", "v"]))
            try:
                self._board.set_piece(Piece(self.color, coordinate))
                break
            except (PieceCoordinateError, BoardError):
                continue
        print("random")
        super(GMAI, self).move(coordinate)

    def coordinate_exchange(self, coordinate):  # 坐标转换函数
        x, y = coordinate
        type = 'h' if x % 2 == 0 else 'v'
        x = x if x % 2 == 0 else x+1
        x = str(int(6 - x / 2))
        y = ['a', 'b', 'c', 'd', 'e', 'f'][y//2]
        return (y, x, type)
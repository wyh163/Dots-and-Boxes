# -*- coding: UTF-8 -*-
from enum import Enum


class Color(Enum):
    red = 1
    blue = 2


class DBException(Exception):
    pass


class Player:
    def __init__(self, color):
        self._color = color
        self.score = 0

    @property
    def color(self):
        return self._color


class Piece:
    def __init__(self, player, user_coordinate):  # 坐标合法性检查在坐标转换函数中完成
        self._player = player
        self._coordinate = self._coordinate_exchange(user_coordinate)  # 坐标转换，把('b', '4', 'v')转换为(3, 2)
        self._user_coordinate = user_coordinate  # 用户坐标，如('b', '4', 'v')

    @property
    def player(self):
        return self._player

    @property
    def color(self):
        return self._player.color()

    @property
    def coordinate(self):
        return self._coordinate

    @property
    def user_coordinate(self):
        return self._user_coordinate

    def _coordinate_exchange(self, coordinate):  # 坐标转换函数
        x = 12 - 2 * int(coordinate[1])

        if (coordinate[0] == 'a'):
            y = 0
        elif (coordinate[0] == 'b'):
            y = 2
        elif (coordinate[0] == 'c'):
            y = 4
        elif (coordinate[0] == 'd'):
            y = 6
        elif (coordinate[0] == 'e'):
            y = 8
        elif (coordinate[0] == 'f'):
            y = 10
        else:
            raise PieceCoordinateError("Wrong piece coordinate.")

        if (coordinate[2] == 'v'):
            x = x - 1
        elif (coordinate[2] == 'h'):
            y = y + 1
        else:
            raise PieceCoordinateError("Wrong piece coordinate.")

        if (x > 10 or y > 10 or (x + y) % 2 == 0):  # 判断转换的坐标是否合法，当坐标为点或格子时，x+y为偶数
            raise PieceCoordinateError("Wrong piece coordinate.")

        return (x, y)


class PieceCoordinateError(DBException):
    def __init__(self, *args, **kwargs):
        pass


class Board:
    def __init__(self):
                       #  0   1   2   3   4   5   6   7   8   9  10
        self._pieces = [[-1,  0, -1,  0, -1,  0, -1,  0, -1,  0, -1],  # 0
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # 1
                        [-1,  0, -1,  0, -1,  0, -1,  0, -1,  0, -1],  # 2
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # 3
                        [-1,  0, -1,  0, -1,  0, -1,  0, -1,  0, -1],  # 4
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # 5
                        [-1,  0, -1,  0, -1,  0, -1,  0, -1,  0, -1],  # 6
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # 7
                        [-1,  0, -1,  0, -1,  0, -1,  0, -1,  0, -1],  # 8
                        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # 9
                        [-1,  0, -1,  0, -1,  0, -1,  0, -1,  0, -1]]  #10

    @property
    def pieces(self):
        return self._pieces.copy()

    def set_piece(self, piece):
        x = piece.coordinate[0]
        y = piece.coordinate[1]

        if (not self._pieces[x][y] == 0):  # 如果已有棋子则抛出异常
            raise BoardError("Cannot set piece")

        self._pieces[x][y] = piece

    def set_box(self, coordinate, box):
        x = coordinate[0]
        y = coordinate[1]

        if (not self._pieces[x][y] == 0):  # 如果格子已被占领则抛出异常
            raise BoardError("Cannot set box")

        self._pieces[x][y] = box

    def unset_piece(self, piece):
        x = piece.coordinate[0]
        y = piece.coordinate[1]

        if (self._pieces[x][y] == 0):  # 如果没有棋子则抛出异常
            raise BoardError("Cannot unset piece")

        self._pieces[x][y] = 0

    def unset_box(self, coordinate):
        x = coordinate[0]
        y = coordinate[1]

        if (self._pieces[x][y] == 0):  # 如果格子未被占领则抛出异常
            raise BoardError("Cannot unset box")

        self._pieces[x][y] = 0


class BoardError(DBException):
    def __init__(self, *args, **kwargs):
        pass


class PieceHistory():
    def __init__(self):
        self._list = []

    @property
    def list(self):
        return self._list.copy()

    @property
    def len(self):
        return len(self._list)

    def add(self, piece):
        self._list.append(piece)

    def delete(self):
        return self._list.pop()


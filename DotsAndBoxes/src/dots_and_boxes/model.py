# coding = UTF-8
from enum import Enum


class Color(Enum):
    red = 1
    blue = 2


class Player:
    def __init__(self, color):
        self._color = color
        self.score = 0

    def color(self):
        return self._color


class Piece:
    def __init__(self, color, coordinate):
        self._color = color
        self._coordinate = coordinate

    def color(self):
        return self._color

    def coordinate(self):
        return self._coordinate


class Board:
    def __init__(self, game_delegate):
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
        self._game_delegate = game_delegate

    def pieces(self):
        return self._pieces

    def move_to(self, piece):
        new_coordinate = self._coordinate_exchange(piece.coordinate)  # 坐标转换，把(B, 4, V)转换为(3, 2)
        x = new_coordinate[0]
        y = new_coordinate[1]

        if (not self._pieces[x][y] == 0):  # 如果已有棋子则抛出异常
            raise PieceError("Wrong piece.")

        self._pieces[x][y] = piece.color.value

        if (piece.coordinate[2] == 'v' or piece.coordinate[2] == 'V'):
            if self._check_box((x, y-1)):  # 判断格坐标合法性的逻辑在_check_box()函数中
                self._game_delegate.add_score(piece.color)
            if self._check_box((x, y+1)):
                self._game_delegate.add_score(piece.color)
        else:
            if self._check_box((x-1, y)):
                self._game_delegate.add_score(piece.color)
            if self._check_box((x+1, y)):
                self._game_delegate.add_score(piece.color)

    def _coordinate_exchange(self, coordinate):  # 坐标转换函数
        x = 12 - 2 * int(coordinate()[1])

        if (coordinate[0] == 'a' or coordinate[0] == 'A'):
            y = 0
        elif (coordinate[0] == 'b' or coordinate[0] == 'B'):
            y = 2
        elif (coordinate[0] == 'c' or coordinate[0] == 'C'):
            y = 4
        elif (coordinate[0] == 'd' or coordinate[0] == 'D'):
            y = 6
        elif (coordinate[0] == 'e' or coordinate[0] == 'E'):
            y = 8
        elif (coordinate[0] == 'f' or coordinate[0] == 'F'):
            y = 10
        else:
            raise PieceCoordinateError("Wrong piece coordinate.")

        if (coordinate[2] == 'v' or coordinate[2] == 'V'):
            x = x - 1
        elif (coordinate[2] == 'h' or coordinate[2] == 'H'):
            y = y + 1
        else:
            raise PieceCoordinateError("Wrong piece coordinate.")

        if (x > 10 or y > 10 or (x + y) % 2 == 0):  # 判断转换的坐标是否合法，当坐标为点或格子时，x+y为偶数
            raise PieceCoordinateError("Wrong piece coordinate.")

        return (x, y)

    def _check_box(self, box_coordinate):
        x = box_coordinate[0]
        y = box_coordinate[1]

        if (x < 0 or x > 10 or y < 0 or y > 10):  # 判断坐标合法性，如果不合法直接返回不得分
            return False

        if (self._pieces[x-1][y] == 0
            or self._pieces[x+1][y] == 0
            or self._pieces[x][y-1] == 0
            or self._pieces[x][y+1] == 0):
            return False
        else:
            return True


class PieceError(Exception):
    def __init__(self, *args, **kwargs):
        pass


class PieceCoordinateError(Exception):
    def __init__(self, *args, **kwargs):
        pass


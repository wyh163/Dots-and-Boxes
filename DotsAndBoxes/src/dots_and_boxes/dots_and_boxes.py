# -*- coding: UTF-8 -*-
from .game import *
from .model import Color, _Player
import json


class DotsAndBoxes:
    def __init__(self):
        self._current_game = None
        self._history = None
        self._current_move = None
        self._current_step = None
        self._red_player = None
        self._blue_player = None

    @property
    def current_game(self):
        return self._current_game

    @property
    def history(self):
        return self._history.copy()

    @property
    def last_move(self):
        if (self._current_game == None or self._current_step == 0):
            raise DBError("Do not have step")
        return (self._current_step, self._history[self._current_step-1])

    @property
    def red_player(self):
        return self._red_player
    @red_player.setter
    def red_player(self, value):
        if (not value.color == Color.red):
            raise DBError("Invalid players", value)

        if (not self._current_game == None):
            if (not self._current_game.is_end):
                raise DBError("Current game is not over")

        self._red_player = value

    @property
    def blue_player(self):
        return self._blue_player
    @blue_player.setter
    def blue_player(self, value):
        if (not value.color == Color.blue):
            raise DBError("Invalid players", value)

        if (not self._current_game == None):
            if (not self._current_game.is_end):
                raise DBError("Current game is not over")

        self._blue_player = value

    @property
    def current_player(self):
        return (self._red_player if self._current_game.current_player_color == Color.red else self._blue_player)

    @property
    def current_step(self):
        return self._current_step

    def new_game(self):
        if (not self._current_game == None):
            if (not self._current_game.is_end):
                raise DBError("Current game is not over")

        if (self._red_player == None or self._blue_player == None):
            raise DBError("Lack of player")

        self._new_game()

    def _new_game(self):
        self._current_game = Game(self._red_player, self._blue_player)
        self._history = []
        self._current_step = 0

    def end_game(self):
        if (self._current_game == None):
            raise DBError("Do not have current game")

        self._current_game = None
        self._history = None
        self._current_move = None
        self._current_step = None

    def _move(self, piece):
        self._current_game.move(piece)

        if (self._current_step < len(self._history)):  # 当从某一历史步直接下新步时 (先行判断可以避免_history越界)
            if (not piece == self._history[self._current_step]):  # 如果新步与历史步的下一步历史不同
                while (self._current_step < len(self._history)):  # 先删除这一历史步之后的数据
                    self._history.pop()
                self._history.append(piece)
        else:
            self._history.append(piece)
        self._current_step = self._current_step + 1

    def move(self, color, user_coordinate):
        if (self._current_game == None):
            raise DBError("Do not have current game")

        if (not color == self._current_game.current_player_color):
            raise MoveError("Player color is wrong")

        piece = Piece(self.current_player, user_coordinate)
        self._move(piece)

    def move_with_str(self, input_str):
        if (self._current_game == None):
            raise DBError("Do not have current game")

        piece = self._str_to_coordinate(input_str)
        self.move(piece[0], piece[1])

    def _str_to_coordinate(self, input_str):
        color = x = y = mode = None
        try:
            if (input_str[0] == 'r' or input_str[0] == 'R'):
                color = Color.red
            elif (input_str[0] == 'b' or input_str[0] == 'B'):
                color = Color.blue
            else:
                raise ValueError()
            if (input_str[2] == 'a' or input_str[2] == 'A'):
                x = 'a'
            elif (input_str[2] == 'b' or input_str[2] == 'B'):
                x = 'b'
            elif (input_str[2] == 'c' or input_str[2] == 'C'):
                x = 'c'
            elif (input_str[2] == 'd' or input_str[2] == 'D'):
                x = 'd'
            elif (input_str[2] == 'e' or input_str[2] == 'E'):
                x = 'e'
            elif (input_str[2] == 'f' or input_str[2] == 'F'):
                x = 'f'
            else:
                raise ValueError()
            y = int(input_str[3])
            if (y < 0 or y > 6):
                raise ValueError()
            if (input_str[5] == 'v' or input_str[5] == 'V'):
                mode = 'v'
            elif (input_str[5] == 'h' or input_str[5] == 'H'):
                mode = 'h'
            else:
                raise ValueError
        except (IndexError, ValueError, TypeError):
            raise DBError("Invalid input", input_str)

        return (color, (x, str(y), mode))

    def back(self):
        if (self._current_game == None):
            raise DBError("Do not have current game")
        if (self._current_step == 0):
            raise DBError("Do not have step")

        self._current_game.back()

        self._current_step = self._current_step - 1

    def turn_to_step(self, step_num):
        if (self._current_game == None):
            raise DBError("Do not have current game")
        if (step_num < 0 or step_num > len(self._history) or step_num == self._current_step):
            raise DBError("Invalid step num")

        while (self._current_step > step_num):
            self.back()

        while (self._current_step < step_num):
            self._move(self._history[self._current_step])

    def _data_as_dict(self):
        if (self._current_game == None):
            raise DBError("Do not have current game")
        if (self._current_step == 0):
            raise DBError("Do not have step data")

        pieces = []
        for piece in self._current_game.history:
            pieces.append({"timestamp": piece.datetime.timestamp(),
                           "player": "r" if piece.color == Color.red else "b",
                           "coordinate": "".join(piece.user_coordinate)})

        dict = {"R": self._red_player.name,
                "B": self._blue_player.name,
                "is_end": self._current_game.is_end,
                "timestamp": self._current_game.datetime.timestamp(),
                "pieces": pieces}
        if (self._current_game.is_end):
            dict["winner"] = "R" if self._current_game.winner == Color.red else "B"
        return dict

    def save_to_file(self, file_path, mode=1, event=None):
        dict = self._data_as_dict()
        #'''
        if (mode == 0):  # 非常智障的模式
            if (not self._current_game.is_end):
                raise DBError("Current game is not over")
            if (event == None):
                raise DBError("Invalid event")

            pieces_str = ""
            for piece in self._current_game.history:
                if (piece.color == Color.red):
                    pieces_str = pieces_str + "r"
                else:
                    pieces_str = pieces_str + "b"
                pieces_str = pieces_str + "("
                pieces_str = pieces_str + "".join(piece.user_coordinate[0:2])
                pieces_str = pieces_str + ","
                pieces_str = pieces_str + "".join(piece.user_coordinate[2])
                pieces_str = pieces_str + ");"
            dict = {"R": self._red_player.name,
                    "B": self._blue_player.name,
                    "winner": "R" if self._current_game.winner == Color.red else "B",
                    "Date": self._current_game.datetime.strftime("%Y-%m-%d"),
                    "Event": event,
                    "game": pieces_str}
            file_path = file_path + "DB：" + self._red_player.name + " vs " + self._blue_player.name + "："
            file_path = file_path + ("先手胜" if self._current_game.winner == Color.red else "后手胜")
            file_path = file_path + ".txt"#'''

        f = open(file_path, 'w')
        f.write(json.dumps(dict))
        f.close()

        return True

    def load_from_file(self, file_path, mode=1):
        f = open(file_path, 'r')
        file_data = f.read()
        f.close()
        if (mode == 0):  # 非常智障的模式
            data = json.loads(file_data)
            self._red_player = Player.RedPlayer(data['R'])
            self._blue_player = Player.BluePlayer(data['B'])
            self._new_game()
            step_str_arr = data['game'].split(';')
            step_str_arr.pop()
            for step_str in step_str_arr:
                self.move_with_str(step_str)
        else:
            data = json.loads(file_data)
            self._red_player = Player.RedPlayer(data['R'])
            self._blue_player = Player.BluePlayer(data['B'])
            self._new_game()
            for step_data in data['pieces']:
                self.move(Color.red if step_data['player'] == 'r' else Color.blue, (step_data['coordinate'][0], step_data['coordinate'][1], step_data['coordinate'][2]))



class DBError(DBException):
    def __init__(self, *args, **kwargs):
        super(DBError, self).__init__(args, kwargs)


class Player(_Player):
    def __init__(self, color, name):
        super(Player, self).__init__(color)
        self._name = name

    @property
    def name(self):
        return self._name

    @staticmethod
    def RedPlayer(name):
        return Player(Color.red, name)

    @staticmethod
    def BluePlayer(name):
        return Player(Color.blue, name)


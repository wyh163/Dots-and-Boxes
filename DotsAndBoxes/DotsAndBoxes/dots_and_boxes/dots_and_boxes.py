# -*- coding: UTF-8 -*-
import json, time

from .game import *
from .player import *


class DotsAndBoxes:
    def __init__(self, window_controller=None):
        self._current_game = None
        self._history = None
        self._current_step = None
        self._red_player = None
        self._blue_player = None
        self._window_controller = window_controller
        self._update_time = time.time()

    @property
    def current_game(self):
        return self._current_game

    @property
    def history(self):
        return self._history.copy()

    @property
    def last_move(self):
        if (self._current_game == None or self._current_step == 0):
            return None
        return self._history[self._current_step-1]

    @property
    def red_player(self):
        return self._red_player
    @red_player.setter
    def red_player(self, value):
        if (value.color != Color.red):
            raise DBError("Invalid players", value)

        if (self._current_game != None):
            if (not self._current_game.is_end):
                raise DBError("Current game is not over")

        self._red_player = value

    @property
    def blue_player(self):
        return self._blue_player
    @blue_player.setter
    def blue_player(self, value):
        if (value.color != Color.blue):
            raise DBError("Invalid players", value)

        if (self._current_game != None):
            if (not self._current_game.is_end):
                raise DBError("Current game is not over")

        self._blue_player = value

    @property
    def current_player(self):
        return (self._red_player if self._current_game.current_player_color == Color.red else self._blue_player)

    @property
    def current_step(self):
        # int 返回当前步数
        return self._current_step

    @property
    def need_update(self, last_update_time):
        return self._update_time > last_update_time

    def _update(self):
        self._update_time = time.time()

        if (self._window_controller != None):
            self._window_controller.update()

        if self.current_game.is_end:
            self.red_player._game_is_over(self.current_game.winner == Color.red)
            self.blue_player._game_is_over(self.current_game.winner == Color.blue)
        else:
            if isinstance(self.red_player, AIPlayer):
                self.red_player.last_move(self.last_move, self._current_game.board, self._current_game.history, self.current_player.color)
            if isinstance(self.blue_player, AIPlayer):
                self.blue_player.last_move(self.last_move, self._current_game.board, self._current_game.history, self.current_player.color)

    def new_game(self):
        if (self._current_game != None):
            if (not self._current_game.is_end):
                raise DBError("Current game is not over")

        if (self._red_player == None or self._blue_player == None):
            raise DBError("Lack of player")

        self._new_game()

        self._update()

    def _new_game(self):
        self._current_game = Game(self._red_player, self._blue_player)
        self._history = []
        self._current_step = 0

    def end_game(self):
        if (self._current_game == None):
            raise DBError("Do not have current game")

        self._current_game = None
        self._history = None
        self._current_step = None

    def _move(self, piece):
        self._current_game.move(piece)

        if (self._current_step < len(self._history)):  # 当从某一历史步直接下新步时 (先行判断可以避免_history越界)
            if (piece != self._history[self._current_step]):  # 如果新步与历史步的下一步历史不同
                while (self._current_step < len(self._history)):  # 先删除这一历史步之后的数据
                    self._history.pop()
                self._history.append(piece)
        else:
            self._history.append(piece)
        self._current_step = self._current_step + 1

    def move(self, piece):
        if (self._current_game == None):
            raise DBError("Do not have current game")
        if (piece.color != self._current_game.current_player_color):
            raise MoveError("Player color is wrong")

        self._move(piece)

        self._update()

    def move_with_str(self, input_str):
        (color, user_coordinate) = self._str_to_coordinate(input_str)
        if (color != self._current_game.current_player_color):
            raise MoveError("Player color is wrong")

        self.move(Piece(color, user_coordinate))

    def _str_to_coordinate(self, input_str):
        color = x = y = type = None
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
                type = 'v'
            elif (input_str[5] == 'h' or input_str[5] == 'H'):
                type = 'h'
            else:
                raise ValueError
        except (IndexError, ValueError, TypeError):
            raise DBError("Invalid input", input_str)

        return (color, (x, str(y), type))

    def _back(self):
        self._current_game.back()
        self._current_step = self._current_step - 1

    def back(self):
        if (self._current_game == None):
            raise DBError("Do not have current game")
        if (self._current_step == 0):
            raise DBError("Do not have step")

        self._back()

        self._update()

    def turn_to_step(self, step_num):
        if (self._current_game == None):
            raise DBError("Do not have current game")
        if (step_num < 0 or step_num > len(self._history) or step_num == self._current_step):
            raise DBError("Invalid step num")

        while (self._current_step > step_num):
            self._back()
        while (self._current_step < step_num):
            self._move(self._history[self._current_step])

        self._update()

    def _data_as_dict(self):
        if (self._current_game == None):
            raise DBError("Do not have current game")
        if (self._current_step == 0):
            raise DBError("Do not have step data")

        pieces = []
        for piece in self._current_game.history:
            piece_dict = {"timestamp": piece.datetime.timestamp(),
                           "player": "r" if piece.color == Color.red else "b",
                           "coordinate": "".join(piece.user_coordinate)}
            if piece.annotation != "":
                piece_dict["annotation"] = piece.annotation
            pieces.append(piece_dict)

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

            pieces_arr = []
            for piece in self._current_game.history:
                piece_str = ""
                if (piece.color == Color.red):
                    piece_str = piece_str + "r"
                else:
                    piece_str = piece_str + "b"
                piece_str = piece_str + "(" + "".join(piece.user_coordinate[0:2]) + "," + "".join(piece.user_coordinate[2]) + ")"
                piece_dict = {"piece": piece_str}
                if piece.annotation != "":
                    piece_dict["annotation"] = piece.annotation
                pieces_arr.append(piece_dict)
            dict = {"R": self._red_player.name,
                    "B": self._blue_player.name,
                    "winner": "R" if self._current_game.winner == Color.red else "B",
                    "RScore": self._red_player.score,
                    "BScore": self._blue_player.score,
                    "Date": self._current_game.datetime.strftime("%Y-%m-%d"),
                    "Event": event,
                    "game": pieces_arr}
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
            self._red_player = HumanPlayer(Color.red, data['R'], self)
            self._blue_player = HumanPlayer(Color.blue, data['B'], self)
            self._new_game()
            for step in data['game']:
                self.move_with_str(step["piece"])
        else:
            data = json.loads(file_data)
            self._red_player = HumanPlayer(Color.red, data['R'], self)
            self._blue_player = HumanPlayer(Color.blue, data['B'], self)
            self._new_game()
            for step_data in data['pieces']:
                piece = Piece(Color.red if step_data['player'] == 'r' else Color.blue, (step_data['coordinate'][0], step_data['coordinate'][1], step_data['coordinate'][2]))
                self.move(piece)

    def set_piece_annotation(self, step_num, annotation):
        if (self._current_game == None):
            raise DBError("Do not have current game")
        if (step_num < 0 or step_num > len(self._history)):
            raise DBError("Invalid step num")

        self._history[step_num].annotation = annotation


class DBError(DBException):
    def __init__(self, *args, **kwargs):
        super(DBError, self).__init__(args, kwargs)


# -*- coding: UTF-8 -*-
import threading, queue, socket, random, time, json

from ..player import AIPlayer
from ..model import *


class PLFAI(AIPlayer):
    def __init__(self, color, name, game_controller, ser_ip="0.0.0.0", ser_port=33301):
        super(PLFAI, self).__init__(color, name, game_controller)
        self._game_controller = game_controller
        self.ser_ip = ser_ip
        self.ser_port = ser_port
        self.move_queue = None
        self.socket = None
        self.turn = 0

        self.timeout = 10
        self.algorithm = "PV-MCTS"

    def start_new_game(self):
        self.move_queue = queue.Queue()
        self.turn = 0

    def game_is_over(self, is_win):
        pass

    def last_move(self, piece, board, history, next_player_color):
        self._board = board
        self._history = history
        self._last_piece = piece
        self.turn = 0
        if len(history) <= 1:
            self.turn = len(history)
        else:
            for i in range(1, len(history)):
                if history[i].color != history[i-1].color:
                    self.turn = self.turn + 1
            if next_player_color != history[-1].color:
                    self.turn = self.turn + 1

        if (next_player_color == self.color):
            self.__thread = threading.Thread(target=self.move)
            self.__thread.start()

    def move(self):
        if not self.move_queue.empty():
            super(PLFAI, self).move(self.move_queue.get())
            return

        # ==================== Bipedal Bit: Modified for tf-dab ====================
        # In tf-dab server R means the first player and B means the second one.
        # In GUI client red means human player and blue means robot player.
        R, B = {}, {}
        pieces = self._board.pieces
        # Box belong stats
        # 左上角为起始零点，先行后列，从0编号，编号即为左移位数
        R['box'], B['box'] = 0, 0
        for i in range(5):
            for j in range(5):
                if pieces[i*2+1][j*2+1] != 0:
                    c = (pieces[i*2+1][j*2+1])[0]
                    if c == Color.red:
                        R['box'] |= (1 << (i * 5 + j))
                    elif c == Color.blue:
                        B['box'] |= (1 << (i * 5 + j))
        # Edge belong stats
        # 左上角为起始零点，先行后列，从0编号，编号即为左移位数
        R['H'], R['V'], B['H'], B['V'] = 0, 0, 0, 0
        for i in range(6):
            for j in range(5):
                if pieces[i*2][j*2+1] != 0:
                    c = pieces[i*2][j*2+1].color
                    if c == Color.red:
                        R['H'] |= (1 << (i * 5 + j))
                    elif c == Color.blue:
                        B['H'] |= (1 << (i * 5 + j))
        for i in range(5):
            for j in range(6):
                if pieces[i*2+1][j*2] != 0:
                    c = pieces[i*2+1][j*2].color
                    if c == Color.red:
                        R['V'] |= (1 << (i * 6 + j))
                    elif c == Color.blue:
                        B['V'] |= (1 << (i * 6 + j))
        # As the reason mentioned above, may need a switch.
        if self.color == Color.red:
            R, B = B, R
            s1 = self._game_controller.red_player.score
            s0 = self._game_controller.blue_player.score
            now = 0
        else:
            s0 = self._game_controller.red_player.score
            s1 = self._game_controller.blue_player.score
            now = 1
        arg = {
            "id": int(time.time()),
            "params": {
                "Algorithm": self.algorithm,
                "Board": {"R": R, "B": B, "S": [s0, s1], "Now": now, "Turn": self.turn},
                "Timeout": self.timeout
            }
        }

        self.socket = socket.create_connection((self.ser_ip, self.ser_port))
        self.socket.sendall(json.dumps(arg).encode())

        raw_data = self.socket.recv(1024).decode()
        self.socket.close()
        json_data = json.loads(raw_data)
        ms = (json_data["result"]["H"], json_data["result"]["V"])
        moves = []
        for i in range(2):
            for n in range(30):
                if ((1 << n) & ms[i]) != 0:
                    moves.append(self._num2move(((1 << n) | (i << 31))))

        while len(moves) > 1:
            for m in moves:
                p = Piece(self.color, m)
                x, y = p.coordinate
                print((x,y))
                self._board.set_piece(p)
                if (self._check_box((x-1, y)) or self._check_box((x+1, y)) or self._check_box((x, y-1)) or self._check_box((x, y+1))):
                    self.move_queue.put(m)
                    moves.remove(m)
                    break
                else:
                    self._board.unset_piece(p)
        self.move_queue.put(moves[0])

        super(PLFAI, self).move(self.move_queue.get())

    def _num2move(self, value):
        y, x = -1, -1
        if (value & (1 << 31)) != 0:
            type = "h"
        else:
            type = "v"
        for i in range(5)[::1]:
            for j in range(6)[::1]:
                if (value & 1) == 1:
                    if type == "h":
                        y, x = j, i
                    else:
                        y, x = i, j
                    break
                value >>= 1
            if y != -1:
                break

        if type == "h":
            y = str(6 - y)
            x = "abcde"[x]
        else:
            y = str(5 - y)
            x = "abcdef"[x]
        return (x, y, type)

    def _check_box(self, box_coordinate):  # 判断格子是否封闭
        x = box_coordinate[0]
        y = box_coordinate[1]

        if (x < 0 or x > 10 or y < 0 or y > 10):  # 判断坐标是否越界，如果越界直接返回否
            return False
        if (self._board.pieces[x][y] == -1):  # 判断坐标是否为点，如果是点直接返回否
            return False

        if (self._board.pieces[x-1][y] == 0
            or self._board.pieces[x+1][y] == 0
            or self._board.pieces[x][y-1] == 0
            or self._board.pieces[x][y+1] == 0):
            return False

        return True


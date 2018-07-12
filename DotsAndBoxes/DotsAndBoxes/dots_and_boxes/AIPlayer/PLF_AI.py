# -*- coding: UTF-8 -*-
import threading, queue, socket, random, time, json

from ..player import AIPlayer
from ..model import *


# 这是一个AI示例，使用随机算法
class PLFAI(AIPlayer):
    def __init__(self, color, name, game_controller):
        super(PLFAI, self).__init__(color, name, game_controller)
        self._game_controller = game_controller
        # self._comm_thread = _CommThread(self)
        self.move_queue = None
        self.socket = None

        self.timeout = 20
        self.algorithm = "PV-MCTS"

    def start_new_game(self):
        self.move_queue = queue.Queue()

    def game_is_over(self, is_win):
        # 获得比赛结果
        print("You win!" if is_win else "You lose.")

    def last_move(self, piece, board, history, next_player_color):
        self._board = board.pieces
        self._history = history
        self._last_piece = piece
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
        turn = 1
        for i in range(len(self._history)):
            if i == 0:
                turn = turn + 1
            elif self._history[i-1].color != self._history[i].color:
                turn = turn + 1
        # Box belong stats
        R['box'], B['box'] = 0, 0
        for i in range(5):
            for j in range(5):
                if self._board[i*2+1][j*2+1] != 0:
                    c = (self._board[i*2+1][j*2+1])[0]
                    if c == Color.red:
                        R['box'] |= (1 << (i * 5 + j))
                    elif c == Color.blue:
                        B['box'] |= (1 << (i * 5 + j))
        # Edge belong stats
        R['H'], R['V'], B['H'], B['V'] = 0, 0, 0, 0
        for i in range(6):
            for j in range(5):
                if self._board[i*2][j*2+1] != 0:
                    c = self._board[i*2][j*2+1].color
                    if c == Color.red:
                        R['H'] |= (1 << (i * 5 + j))
                    elif c == Color.blue:
                        B['H'] |= (1 << (i * 5 + j))
        for i in range(5):
            for j in range(6):
                if self._board[i*2+1][j*2] != 0:
                    c = self._board[i*2+1][j*2].color
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
                "Board": {"R": R, "B": B, "S": [s0, s1], "Now": now, "Turn": turn},
                "Timeout": self.timeout
            }
        }

        self.socket = socket.create_connection(("0.0.0.0", 33301))
        self.socket.sendall(json.dumps(arg).encode())

        raw_data = self.socket.recv(1024).decode()
        self.socket.close()
        json_data = json.loads(raw_data)
        ms = (json_data["result"]["H"], json_data["result"]["V"])
        for i in range(2):
            for n in range(30):
                if ((1 << n) & ms[i]) != 0:
                    self.move_queue.put(self._num2move(((1 << n) | (i << 31))))

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


class _CommThread(threading.Thread):
    def __init__(self, PLFAI):
        super(_CommThread, self).__init__()
        self.setDaemon(True)
        self.PLFAI = PLFAI
        self.receive_queue = Queue.Queue()

    def run(self):
        pass


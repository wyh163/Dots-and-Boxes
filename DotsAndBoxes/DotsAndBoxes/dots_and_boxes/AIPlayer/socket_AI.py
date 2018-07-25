# -*- coding: UTF-8 -*-
import threading, queue, socket, json
from ..player import AIPlayer
from ..model import *


# 这是一个基于Socket通信的AI示例
class SocketAI(AIPlayer):
    def __init__(self, color, name, game_controller, ser_ip="0.0.0.0", ser_port=22222):
        super(SocketAI, self).__init__(color, name, game_controller)
        self._game_controller = game_controller
        self.ser_ip = ser_ip
        self.ser_port = ser_port
        # 设定通信Socket和落子队列
        self.socket = None
        self.move_queue = None

    def start_new_game(self):
        # 开局重置落子队列，并进行一些初始化工作
        self.move_queue = queue.Queue()

    def game_is_over(self, is_win):
        # 获得比赛结果
        print("AI win!" if is_win else "AI lose.")

    def last_move(self, piece, board, history, next_player_color):
        self._board = board
        self._history = history
        self._last_piece = piece
        # 在这里将落子信息和棋盘局面转换为AI服务器所需的信息

        if (next_player_color == self.color):
            self.__thread = threading.Thread(target=self.move)
            self.__thread.start()

    def move(self):
        # 如落子队列有未走的棋子，先按顺序走落子队列里的棋子
        if not self.move_queue.empty():
            super(SocketAI, self).move(self.move_queue.get())
            return

        # 如落子队列已空，则应向AI服务器请求新落子
        # 将AI所需信息整理并转换为自定义的通信格式
        board = self._board
        history = self._history
        arg = {
            "board": board,
            "history": history
        }

        # 创建Socket连接
        self.socket = socket.create_connection((self.ser_ip, self.ser_port))
        # 发送AI所需信息到AI服务器
        self.socket.sendall(json.dumps(arg).encode())

        # 接收服务器返回的落子信息
        raw_data = self.socket.recv(1024).decode()
        self.socket.close()
        # 解析自定义通信格式描述的落子信息
        json_data = json.loads(raw_data)
        moves_data = (json_data["moves"])
        # 按行棋顺序将落子信息加入落子队列
        for move in moves_data:
            self.move_queue.put(move)

        # 最后，将落子队列的第一个棋子作为这次要走的棋子发送
        super(SocketAI, self).move(self.move_queue.get())


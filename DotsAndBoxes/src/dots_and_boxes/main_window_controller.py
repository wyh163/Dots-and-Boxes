# -*- coding: utf-8 -*-
from .dots_and_boxes import *
from .main_window import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QApplication

class MainWindowController:
    def __init__(self):
        self._window = MainWindow(self)
        self._dots_and_boxes = DotsAndBoxes()
        self._dots_and_boxes.red_player = Player.RedPlayer("player1")
        self._dots_and_boxes.blue_player = Player.BluePlayer("player2")

        self._window.historyTableView.horizontalHeader().setHighlightSections(False)
        self._window.historyTableView.verticalHeader().setVisible(False)
        self._window.historyTableView.setEditTriggers (QAbstractItemView.NoEditTriggers)
        self._window.historyTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._window.historyTableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self._history_tableView_model = QStandardItemModel()
        self._window.historyTableView.setModel(self._history_tableView_model)

        self._history_tableView_model.setColumnCount(3)
        self._history_tableView_model.setHorizontalHeaderLabels(["步数", "玩家", "位置"])
        self._history_tableView_model.setHeaderData(0, Qt.Horizontal, "步数")
        self._window.historyTableView.setColumnWidth(0, 35)
        self._window.historyTableView.setColumnWidth(1, 35)
        self._window.historyTableView.setColumnWidth(2, 100)

    @property
    def window(self):
        return self._window

    def piece_button_is_clicked(self, coordinate, sender):
        if (self._dots_and_boxes.current_game == None):
            return
        if (self._dots_and_boxes.current_game.is_end):
            return
        self._dots_and_boxes.move(self._dots_and_boxes.current_player.color, coordinate)
        self.update()

    def new_game(self):
        self._dots_and_boxes.new_game()
        self.update()

    def update(self):
        if (self._dots_and_boxes.current_game == None):
            self._window.set_current_player_color()
            return
        
        self._window.set_current_player_color(self._dots_and_boxes.current_player.color)

        for x in range(11):
            for y in range(11):
                piece = self._dots_and_boxes.current_game.board.pieces[x][y]
                if (piece == -1):
                    continue
                if ((x + y) % 2 == 0):
                    self._window.set_box((str(x), str(y)), piece)
                    continue
                if (piece != 0):
                    self._window.set_piece_color(piece.user_coordinate, piece.color)
                else:
                    self._window.set_piece_color(("abcdef"[int(y/2)], str(int((12-x)/2)), "h" if (x % 2 == 0) else "v"))
        print(self._dots_and_boxes.current_step)
        if (self._dots_and_boxes.current_step != 0):
            step = self._dots_and_boxes.history[self._dots_and_boxes.current_step - 1]
            self._history_tableView_model.setItem(self._dots_and_boxes.current_step - 1, 0, QStandardItem(str(self._dots_and_boxes.current_step)))
            self._history_tableView_model.setItem(self._dots_and_boxes.current_step - 1, 1, QStandardItem("红" if step.color == Color.red else "蓝"))
            self._history_tableView_model.setItem(self._dots_and_boxes.current_step - 1, 2, QStandardItem(step.user_coordinate[0]+step.user_coordinate[1]+step.user_coordinate[2]))


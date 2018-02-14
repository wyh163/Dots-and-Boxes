# -*- coding: utf-8 -*-
from .dots_and_boxes import *
from .main_window import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QPushButton

class MainWindowController:
    def __init__(self):
        self._window = MainWindow(self)
        self._dots_and_boxes = DotsAndBoxes()
        self._dots_and_boxes.red_player = Player.RedPlayer("player1")
        self._dots_and_boxes.blue_player = Player.BluePlayer("player2")

        self._window.history_tableView.horizontalHeader().setHighlightSections(False)
        self._window.history_tableView.verticalHeader().setVisible(False)
        self._window.history_tableView.setEditTriggers (QAbstractItemView.NoEditTriggers)
        self._window.history_tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._window.history_tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self._history_tableView_model = QStandardItemModel()
        self._window.history_tableView.setModel(self._history_tableView_model)

        self._history_tableView_model.setColumnCount(3)
        self._history_tableView_model.setHorizontalHeaderLabels(["步数", "玩家", "位置"])
        self._history_tableView_model.setHeaderData(0, Qt.Horizontal, "步数")
        self._window.history_tableView.setColumnWidth(0, 35)
        self._window.history_tableView.setColumnWidth(1, 35)
        self._window.history_tableView.setColumnWidth(2, 100)

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
        self._window.set_current_player_color(self._dots_and_boxes.current_player.color)
        i = 0
        for step in self._dots_and_boxes.history:
            self._history_tableView_model.setItem(i, 0, QStandardItem(str(i+1)))
            self._history_tableView_model.setItem(i, 1, QStandardItem("红" if step.color == Color.red else "蓝"))
            self._history_tableView_model.setItem(i, 2, QStandardItem(step.user_coordinate[0]+step.user_coordinate[1]+step.user_coordinate[2]))
            self._window.findChild((QPushButton, ), "button"+step.user_coordinate[0]+step.user_coordinate[1]+step.user_coordinate[2]).setStyleSheet("background-color:"+("#ff0000" if step.color == Color.red else "#0055ff"))
            i = i + 1



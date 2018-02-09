# -*- coding: utf-8 -*-
from .dots_and_boxes import *
from .main_window import *
from PyQt5.QtGui import QStandardItemModel
from PyQt5 import QtCore

class MainWindowController:
    def __init__(self):
        self._window = MainWindow(self)
        self._dots_and_boxes = DotsAndBoxes()
        self._history_tableView_model = QStandardItemModel()
        self._window.history_tableView.setModel(self._history_tableView_model)

        self._history_tableView_model.setColumnCount(2)
        self._history_tableView_model.setHeaderData(0, QtCore.Qt.Horizontal, "步数")
        self._history_tableView_model.setHeaderData(1, QtCore.Qt.Horizontal, "位置")
        self._window.history_tableView.setColumnWidth(0, 40)
        self._window.history_tableView.setColumnWidth(1, 185)

    @property
    def window(self):
        return self._window

    def _add_history_cell(self):
        self._history_tableView_model.setHeaderData(0, QtCore.Qt.Horizontal, "步数")



# -*- coding: utf-8 -*-
from .dots_and_boxes import *
from .main_window import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QFileDialog, QDialog, QMessageBox

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

        self.update()

    @property
    def window(self):
        return self._window

    def new_game(self):
        self._dots_and_boxes.new_game()
        self.update()

    def load_game(self):
        fileDialog = QFileDialog()
        fileDialog.setWindowTitle("载入")
        fileDialog.setAcceptMode(QFileDialog.AcceptOpen)
        fileDialog.setFileMode(QFileDialog.AnyFile)
        fileDialog.setViewMode(QFileDialog.Detail)
        fileDialog.setDirectory(".")
        if (fileDialog.exec() == QDialog.Accepted):
            path = fileDialog.selectedFiles()[0]
            self._dots_and_boxes.load_from_file(path)
            self.update()
        fileDialog.show()

    def load_standard_record(self):
        fileDialog = QFileDialog()
        fileDialog.setWindowTitle("载入")
        fileDialog.setAcceptMode(QFileDialog.AcceptOpen)
        fileDialog.setFileMode(QFileDialog.AnyFile)
        fileDialog.setViewMode(QFileDialog.Detail)
        fileDialog.setDirectory(".")
        if (fileDialog.exec() == QDialog.Accepted):
            path = fileDialog.selectedFiles()[0]
            self._dots_and_boxes.load_from_file(path, 0)
            self.update()
        fileDialog.show()

    def end_game(self):
        self._dots_and_boxes.end_game()
        self.update()

    def save_game(self):
        fileDialog = QFileDialog()
        fileDialog.setWindowTitle("保存为")
        fileDialog.setAcceptMode(QFileDialog.AcceptSave)
        fileDialog.setFileMode(QFileDialog.AnyFile)
        fileDialog.setViewMode(QFileDialog.Detail)
        fileDialog.setDirectory(".")
        fileDialog.selectFile("DotsAndBoxesRecord.dbr")
        if (fileDialog.exec() == QDialog.Accepted):
            path = fileDialog.selectedFiles()[0]
            self._dots_and_boxes.save_to_file(path)
        fileDialog.show()

    def export_standard_record(self):
        fileDialog = QFileDialog()
        fileDialog.setWindowTitle("保存到")
        fileDialog.setAcceptMode(QFileDialog.AcceptSave)
        fileDialog.setFileMode(QFileDialog.Directory)
        fileDialog.setViewMode(QFileDialog.Detail)
        fileDialog.setDirectory(".")
        if (fileDialog.exec() == QDialog.Accepted):
            path = fileDialog.selectedFiles()[0]
            self._dots_and_boxes.save_to_file(path + "/", 0, "")
        fileDialog.show()

    def piece_button_is_clicked(self, coordinate, sender):
        if (self._dots_and_boxes.current_game == None):
            return
        if (self._dots_and_boxes.current_game.is_end):
            return
        self._dots_and_boxes.move(self._dots_and_boxes.current_player.color, coordinate)
        self.update()
        if (self._dots_and_boxes.current_game.is_end):
            msgBox = QMessageBox(QMessageBox.NoIcon, "游戏结束", "红方获胜" if self._dots_and_boxes.current_game.winner == Color.red else "蓝方获胜", QMessageBox.Ok, self._window)
            msgBox.show()
            print("asd")

    def back(self):
        self._dots_and_boxes.back()
        self.update()

    def forward(self):
        self._dots_and_boxes.turn_to_step(self._dots_and_boxes.current_step + 1)
        self.update()

    def update(self):
        if (self._dots_and_boxes.current_game == None):
            self._window.newGameAction.setEnabled(True)
            self._window.loadGameAction.setEnabled(True)
            self._window.loadStandardRecordAction.setEnabled(True)
            self._window.endGameAction.setEnabled(False)
            self._window.saveGameAction.setEnabled(False)
            self._window.exportStandardRecordAction.setEnabled(False)
            self._window.backAction.setEnabled(False)
            self._window.forwardAction.setEnabled(False)

            self.set_current_player_color()
            self.set_current_step(0)
            self.set_red_player_score(0)
            self.set_blue_player_score(0)

            # 棋子
            for x in "abcdef":
                for y in range(1, 6):
                    piece = self._window.findChild((QtWidgets.QPushButton,), "button" + x + str(y) + "v")
                    piece.setStyleSheet("background-color:#ffffff")
                    piece.setEnabled(False)
            for x in "abcde":
                for y in range(1, 7):
                    piece = self._window.findChild((QtWidgets.QPushButton,), "button" + x + str(y) + "h")
                    piece.setStyleSheet("background-color:#ffffff")
                    piece.setEnabled(False)
            # 格
            for x in range(1, 10, 2):
                for y in range(1, 10, 2):
                    self.set_box((str(x), str(y)), 0)

            self._history_tableView_model.removeRows(0, self._history_tableView_model.rowCount())
            return

        self._window.newGameAction.setEnabled(False)
        self._window.loadGameAction.setEnabled(False)
        self._window.loadStandardRecordAction.setEnabled(False)
        self._window.endGameAction.setEnabled(True)
        if (not self._dots_and_boxes.current_game == None):
            self._window.saveGameAction.setEnabled(not len(self._dots_and_boxes.history) == 0)
        else:
            self._window.saveGameAction.setEnabled(False)
        self._window.exportStandardRecordAction.setEnabled(self._dots_and_boxes.current_game.is_end)
        self._window.backAction.setEnabled(self._dots_and_boxes.current_step > 0)
        self._window.forwardAction.setEnabled(self._dots_and_boxes.current_step < len(self._dots_and_boxes.history))

        # 刷新信息
        self.set_current_player_color(self._dots_and_boxes.current_player.color)
        self.set_current_step(self._dots_and_boxes.current_step + 1)
        self.set_red_player_score(self._dots_and_boxes.red_player.score)
        self.set_blue_player_score(self._dots_and_boxes.blue_player.score)
        # 刷新棋盘
        for x in range(11):
            for y in range(11):
                piece = self._dots_and_boxes.current_game.board.pieces[x][y]
                if (piece == -1):
                    continue
                if ((x + y) % 2 == 0):
                    self.set_box((str(x), str(y)), piece)
                    continue
                if (piece != 0):
                    self.set_piece_color(piece.user_coordinate, piece.color)
                else:
                    self.set_piece_color(("abcdef"[int(y/2)], str(int((12-x)/2)), "h" if (x % 2 == 0) else "v"))
        # 刷新历史信息
        # self._history_tableView_model.removeRows(0, self._history_tableView_model.rowCount())
        for step in self._dots_and_boxes.history:
            self._history_tableView_model.setItem(self._dots_and_boxes.history.index(step), 0, QStandardItem(str(self._dots_and_boxes.history.index(step) + 1)))
            self._history_tableView_model.setItem(self._dots_and_boxes.history.index(step), 1, QStandardItem("红" if step.color == Color.red else "蓝"))
            self._history_tableView_model.setItem(self._dots_and_boxes.history.index(step), 2, QStandardItem(step.user_coordinate[0]+step.user_coordinate[1]+step.user_coordinate[2]))
        self._history_tableView_model.removeRows(len(self._dots_and_boxes.history), self._history_tableView_model.rowCount() - len(self._dots_and_boxes.history))
        self._window.historyTableView.scrollToBottom()

    def set_piece_color(self, coordinate, color=None):
        piece = self._window.findChild((QtWidgets.QPushButton, ), "button" + coordinate[0] + coordinate[1] + coordinate[2])
        if (color == Color.red):
            piece.setStyleSheet("background-color:#ff0000")
            piece.setEnabled(False)
            return
        if (color == Color.blue):
            piece.setStyleSheet("background-color:#0055ff")
            piece.setEnabled(False)
            return
        piece.setStyleSheet("background-color:#ffffff")
        piece.setEnabled(True)

    def set_box(self, coordinate, info=0):
        box = self._window.findChild((QtWidgets.QLabel,), "boxLabel" + coordinate[0] + coordinate[1])
        if (info == 0):
            box.setStyleSheet("background-color:#ffffff")
            box.setText("")

        else:
            player = info[0]
            num = info[1]
            if (player.color == Color.red):
                box.setStyleSheet("background-color:#ff0000")
            else:
                box.setStyleSheet("background-color:#0055ff")
            box.setText("<html><head/><body><p><span style=\" color:#ffffff;\">" + str(num) + "</span></p></body></html>")

    def set_current_player_color(self, color=None):
        if (color == Color.red):
            self._window.currentPlayerLabel.setText("<html><head/><body><p><span style=\" color:#ff0000;\">•</span></p></body></html>")
            return
        if (color == Color.blue):
            self._window.currentPlayerLabel.setText("<html><head/><body><p><span style=\" color:#0055ff;\">•</span></p></body></html>")
            return
        self._window.currentPlayerLabel.setText("")

    def set_red_player_score(self, score):
        self._window.redScoreNumber.display(score)

    def set_blue_player_score(self, score):
        self._window.blueScoreNumber.display(score)

    def set_current_step(self, step):
        self._window.currentStepLabel.setText(str(step))

    def set_history_table_view_place(self, percent):
        pass


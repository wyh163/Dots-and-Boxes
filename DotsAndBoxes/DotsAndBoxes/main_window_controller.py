# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt, QDir, pyqtSignal
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QFileDialog, QDialog, QMessageBox, QInputDialog, QLineEdit, QAbstractItemView, QWidget

from .dots_and_boxes.dots_and_boxes import *
from .dots_and_boxes.player import *
from .main_window import *

from .dots_and_boxes.AIPlayer.random_AI import RandomAI


class MainWindowController(QWidget):
    _updateSignal = pyqtSignal()

    def __init__(self):
        super(MainWindowController, self).__init__()
        self._window = MainWindow()

        self._window.historyTableView.horizontalHeader().setHighlightSections(False)
        self._window.historyTableView.verticalHeader().setVisible(False)
        self._window.historyTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self._window.historyTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._window.historyTableView.setSelectionMode(QAbstractItemView.SingleSelection)
        # 关键历史信息表的双击事件为转到特定步
        self._window.historyTableView.doubleClicked.connect(lambda index: self.turn_to_step(index.row() + 1))
        self._history_tableView_model = QStandardItemModel()
        self._window.historyTableView.setModel(self._history_tableView_model)

        self._history_tableView_model.setColumnCount(3)
        self._history_tableView_model.setHorizontalHeaderLabels(["步数", "玩家", "位置"])
        self._history_tableView_model.setHeaderData(0, Qt.Horizontal, "步数")
        self._window.historyTableView.setColumnWidth(0, 35)
        self._window.historyTableView.setColumnWidth(1, 35)
        self._window.historyTableView.setColumnWidth(2, 100)

        self._window.newGameAction.triggered.connect(self.new_game)
        self._window.loadGameAction.triggered.connect(self.load_game)
        self._window.endGameAction.triggered.connect(self.end_game)
        self._window.saveGameAction.triggered.connect(self.save_game)
        self._window.backAction.triggered.connect(self.back)
        self._window.forwardAction.triggered.connect(self.forward)
        self._window._turnToStartAction.triggered.connect(lambda t, step=0: self.turn_to_step(step))
        self._window._turnToEndAction.triggered.connect(self._turn_to_end)
        self._window.setRedPlayerAction.triggered.connect(self.set_red_player)
        self._window.setBluePlayerAction.triggered.connect(self.set_blue_player)
        self._window.loadStandardRecordAction.triggered.connect(self.load_standard_record)
        self._window.exportStandardRecordAction.triggered.connect(self.export_standard_record)
        self._window.setPieceAnnotationAction.triggered.connect(self._set_piece_annotation)
        
        for x in "abcdef":
            for y in range(1, 6):
                button = self._window.findChild((QtWidgets.QPushButton, ), "button" + x + str(y) + "v")
                button.clicked.connect(lambda t, c=(x, str(y), "v"), b=button: self.piece_button_is_clicked(c, b))
        for x in "abcde":
            for y in range(1, 7):
                button = self._window.findChild((QtWidgets.QPushButton, ), "button" + x + str(y) + "h")
                button.clicked.connect(lambda t, c=(x, str(y), "h"), b=button: self.piece_button_is_clicked(c, b))

        self._updateSignal.connect(self._update)

        self._dots_and_boxes = DotsAndBoxes(self)
        self.update()

        self._wait_piece_annotation = ""

    @property
    def window(self):
        return self._window

    def new_game(self):
        try:
            self._dots_and_boxes.new_game()
        except DBError as e:
            msgBox = QMessageBox(QMessageBox.Warning, "异常", e.info, QMessageBox.Ok, self._window)
            msgBox.show()
        self.update()

    def load_game(self):
        file_path = QFileDialog.getOpenFileName(caption="载入", directory=QDir.homePath())[0]
        if (file_path != ""):
            try:
                self._dots_and_boxes.load_from_file(file_path)
            except Exception as e:
                msgBox = QMessageBox(QMessageBox.Warning, "异常", "载入错误！\n请检查选择的文件是否正确。\n载入大学生计算机博弈大赛点格棋标准棋谱文件，请选择 ->工具 ->载入标准棋谱。", QMessageBox.Ok, self._window)
                msgBox.show()
                self._dots_and_boxes = DotsAndBoxes()
            self.update()

    def end_game(self):
        self._dots_and_boxes.end_game()
        self.update()

    def save_game(self):
        fileDialog = QFileDialog()
        fileDialog.setWindowTitle("保存为")
        fileDialog.setAcceptMode(QFileDialog.AcceptSave)
        fileDialog.setFileMode(QFileDialog.AnyFile)
        fileDialog.setViewMode(QFileDialog.Detail)
        fileDialog.setDirectory(QDir.homePath())
        fileDialog.selectFile("DotsAndBoxesRecord.dbr")
        if (fileDialog.exec() == QDialog.Accepted):
            path = fileDialog.selectedFiles()[0]
            self._dots_and_boxes.save_to_file(path)
        fileDialog.show()

    def load_standard_record(self):
        file_path = QFileDialog.getOpenFileName(caption="载入标准棋谱", directory=QDir.homePath())[0]
        if (file_path != ""):
            try:
                self._dots_and_boxes.load_from_file(file_path, 0)
            except Exception as e:
                msgBox = QMessageBox(QMessageBox.Warning, "异常", "载入错误！\n请检查文件是否符合大学生计算机博弈大赛点格棋标准棋谱格式。", QMessageBox.Ok, self._window)
                msgBox.show()
                self._dots_and_boxes = DotsAndBoxes()
            self.update()

    def export_standard_record(self):
        event, ok = QInputDialog.getText(self._window, "比赛信息", "请输入比赛名称:", QLineEdit.Normal, "大学生计算机博弈大赛")
        if (not ok):
            return
        file_path = QFileDialog.getExistingDirectory(caption="导出标准棋谱到", directory=QDir.homePath())
        if (file_path != ""):
            self._dots_and_boxes.save_to_file(file_path + "/", 0, event)

    def set_red_player(self):
        red_player_name, ok = QInputDialog.getText(self._window, "设定红方玩家", "请输入红方玩家名称:", QLineEdit.Normal, "RedPlayer")
        if (not ok):
            return
        try:
            self._dots_and_boxes.red_player = HumanPlayer(Color.red, red_player_name, self._dots_and_boxes)
        except DBError as e:
            msgBox = QMessageBox(QMessageBox.Warning, "异常", e.info, QMessageBox.Ok, self._window)
            msgBox.show()

    def set_blue_player(self):
        blue_player_name, ok = QInputDialog.getText(self._window, "设定蓝方玩家", "请输入蓝方玩家名称:", QLineEdit.Normal, "BluePlayer")
        if (not ok):
            return
        try:
            self._dots_and_boxes.blue_player = HumanPlayer(Color.blue, blue_player_name, self._dots_and_boxes)
        except DBError as e:
            msgBox = QMessageBox(QMessageBox.Warning, "异常", e.info, QMessageBox.Ok, self._window)
            msgBox.show()

    def _set_piece_annotation(self):
        self._wait_piece_annotation, ok = QInputDialog.getText(self._window, "添加注释", "注释内容:", QLineEdit.Normal, "")
        if (not ok):
            self._wait_piece_annotation = ""
            return
        else:
            if (self._dots_and_boxes.current_step <= len(self._dots_and_boxes.history)):
                self._dots_and_boxes.set_piece_annotation(self._dots_and_boxes.current_step-1, self._wait_piece_annotation)
                self._wait_piece_annotation = ""

    def piece_button_is_clicked(self, coordinate, sender):
        if (self._dots_and_boxes.current_game == None):
            return
        if (self._dots_and_boxes.current_game.is_end):
            return

        if isinstance(self._dots_and_boxes.current_player, AIPlayer):
            return

        self._dots_and_boxes.current_player.move(coordinate)

        if self._wait_piece_annotation != "":
            self._dots_and_boxes.set_piece_annotation(self._dots_and_boxes.current_step-1, self._wait_piece_annotation)
            self._wait_piece_annotation = ""

    def back(self):
        self._dots_and_boxes.back()
        self.update()

    def forward(self):
        self._dots_and_boxes.turn_to_step(self._dots_and_boxes.current_step + 1)
        self.update()

    def turn_to_step(self, step_num):
        if (step_num == self._dots_and_boxes.current_step):
            return
        self._dots_and_boxes.turn_to_step(step_num)
        self.update()

    # !!!警告!!! 这是一个临时api，将在之后的版本中删掉
    def _turn_to_end(self):
        self.turn_to_step(len(self._dots_and_boxes.history))

    def update(self):
        self._updateSignal.emit()

    def _update(self):
        if (self._dots_and_boxes.current_game == None):
            self._window.newGameAction.setEnabled(True)
            self._window.loadGameAction.setEnabled(True)
            self._window.loadStandardRecordAction.setEnabled(True)
            self._window.endGameAction.setEnabled(False)
            self._window.saveGameAction.setEnabled(False)
            self._window.exportStandardRecordAction.setEnabled(False)
            self._window.backAction.setEnabled(False)
            self._window.forwardAction.setEnabled(False)
            self._window._turnToStartAction.setEnabled(False)
            self._window._turnToEndAction.setEnabled(False)

            self.set_current_player_color()
            self.set_current_step(0)
            self.set_red_player_score(0)
            self.set_blue_player_score(0)

            # 棋子
            for x in "abcdef":
                for y in range(1, 6):
                    piece_button = self._window.findChild((QtWidgets.QPushButton,), "button" + x + str(y) + "v")
                    piece_button.setStyleSheet("background-color:#ffffff")
                    piece_button.setText("")
                    piece_button.setEnabled(False)
            for x in "abcde":
                for y in range(1, 7):
                    piece_button = self._window.findChild((QtWidgets.QPushButton,), "button" + x + str(y) + "h")
                    piece_button.setStyleSheet("background-color:#ffffff")
                    piece_button.setText("")
                    piece_button.setEnabled(False)
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
        if (self._dots_and_boxes.current_game != None):
            self._window.saveGameAction.setEnabled(len(self._dots_and_boxes.history) != 0)
        else:
            self._window.saveGameAction.setEnabled(False)
        self._window.exportStandardRecordAction.setEnabled(self._dots_and_boxes.current_game.is_end)
        self._window.backAction.setEnabled(self._dots_and_boxes.current_step > 0)
        self._window.forwardAction.setEnabled(self._dots_and_boxes.current_step < len(self._dots_and_boxes.history))
        self._window._turnToStartAction.setEnabled(True)
        self._window._turnToEndAction.setEnabled(True)

        # 刷新信息
        self.set_current_player_color(self._dots_and_boxes.current_player.color)
        self.set_current_step(self._dots_and_boxes.current_step)
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
                    self.set_piece_color(("abcdef"[int(y / 2)], str(int((12 - x) / 2)), "h" if (x % 2 == 0) else "v"))
        # 当前步高亮
        if (self._dots_and_boxes.current_step != 0):
            coordinate = self._dots_and_boxes.history[self._dots_and_boxes.current_step - 1].user_coordinate
            piece_button = self._window.findChild((QtWidgets.QPushButton,), "button" + coordinate[0] + coordinate[1] + coordinate[2])
            piece_button.setText("•")

        # 刷新历史信息
        for step in self._dots_and_boxes.history:
            self._history_tableView_model.setItem(self._dots_and_boxes.history.index(step), 0, QStandardItem(str(self._dots_and_boxes.history.index(step) + 1)))
            self._history_tableView_model.setItem(self._dots_and_boxes.history.index(step), 1, QStandardItem("红" if step.color == Color.red else "蓝"))
            self._history_tableView_model.setItem(self._dots_and_boxes.history.index(step), 2, QStandardItem(step.user_coordinate[0] + step.user_coordinate[1] + step.user_coordinate[2]))
            self._history_tableView_model.item(self._dots_and_boxes.history.index(step), 0).setTextAlignment(Qt.AlignCenter)
            self._history_tableView_model.item(self._dots_and_boxes.history.index(step), 1).setTextAlignment(Qt.AlignCenter)
        self._history_tableView_model.removeRows(len(self._dots_and_boxes.history), self._history_tableView_model.rowCount() - len(self._dots_and_boxes.history))
        # 选中当前步历史信息
        self._window.historyTableView.selectRow(self._dots_and_boxes.current_step - 1)
        # 历史信息滚动到当前步 直接使用scrollTo会导致无法滚动到底部，原因未知，解决方法为判断是否为最后一步，如果是则执行scrollToBottom
        if (self._dots_and_boxes.current_step == len(self._dots_and_boxes.history)):
            self._window.historyTableView.scrollToBottom()
        else:
            self._window.historyTableView.scrollTo(self._history_tableView_model.index(self._dots_and_boxes.current_step - 1, 0), QAbstractItemView.PositionAtCenter)
        # 修复每次刷新后列宽异常的bug，原因未知
        self._window.historyTableView.setColumnWidth(0, 35)
        self._window.historyTableView.setColumnWidth(1, 35)
        self._window.historyTableView.setColumnWidth(2, 100)

        if (self._dots_and_boxes.current_game.is_end):
            msgBox = QMessageBox(QMessageBox.NoIcon, "游戏结束", "红方获胜" if self._dots_and_boxes.current_game.winner == Color.red else "蓝方获胜", QMessageBox.Ok, self._window)
            msgBox.show()

    def set_piece_color(self, coordinate, color=None):
        piece = self._window.findChild((QtWidgets.QPushButton,), "button" + coordinate[0] + coordinate[1] + coordinate[2])
        piece.setText("")
        if (color == Color.red):
            piece.setStyleSheet("color: #ffffff; background-color:#ff0000")
            piece.setEnabled(False)
            return
        if (color == Color.blue):
            piece.setStyleSheet("color: #ffffff; background-color:#0055ff")
            piece.setEnabled(False)
            return
        piece.setStyleSheet("color: #ffffff; background-color:#ffffff")
        piece.setEnabled(True)

    def set_box(self, coordinate, info=0):
        box = self._window.findChild((QtWidgets.QLabel,), "boxLabel" + coordinate[0] + coordinate[1])
        if (info == 0):
            box.setStyleSheet("background-color:#ffffff")
            box.setText("")

        else:
            color = info[0]
            num = info[1]
            if (color == Color.red):
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


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from .model import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 548)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint);
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height());
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(8, 0, 711, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.boardLayout = QtWidgets.QGridLayout()
        self.boardLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.boardLayout.setContentsMargins(0, -1, -1, -1)
        self.boardLayout.setSpacing(0)
        self.boardLayout.setObjectName("boardLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.boardLayout.addItem(spacerItem, 1, 12, 11, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.boardLayout.addItem(spacerItem1, 0, 1, 1, 11)
        self.horizontalLayout.addLayout(self.boardLayout)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setMinimumSize(QtCore.QSize(25, 30))
        self.label_13.setMaximumSize(QtCore.QSize(25, 30))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setIndent(20)
        self.label_13.setMargin(-20)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 3, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setMinimumSize(QtCore.QSize(25, 30))
        self.label_14.setMaximumSize(QtCore.QSize(25, 30))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setIndent(20)
        self.label_14.setMargin(-20)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 3, 3, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_2.setMinimumSize(QtCore.QSize(40, 25))
        self.lcdNumber_2.setMaximumSize(QtCore.QSize(40, 25))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout_3.addWidget(self.lcdNumber_2, 3, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setMinimumSize(QtCore.QSize(0, 35))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 2, 1, 1, 4)
        self.lcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber.setMinimumSize(QtCore.QSize(40, 25))
        self.lcdNumber.setMaximumSize(QtCore.QSize(40, 25))
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_3.addWidget(self.lcdNumber, 3, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 2, 5, 2, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 2, 0, 2, 1)
        self.currentStepTextLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.currentStepTextLabel.setMinimumSize(QtCore.QSize(0, 35))
        self.currentStepTextLabel.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.currentStepTextLabel.setFont(font)
        self.currentStepTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.currentStepTextLabel.setObjectName("currentStepTextLabel")
        self.gridLayout_3.addWidget(self.currentStepTextLabel, 1, 0, 1, 3)
        self.currentPlayerTextLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.currentPlayerTextLabel.setMinimumSize(QtCore.QSize(0, 35))
        self.currentPlayerTextLabel.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.currentPlayerTextLabel.setFont(font)
        self.currentPlayerTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.currentPlayerTextLabel.setObjectName("currentPlayerTextLabel")
        self.gridLayout_3.addWidget(self.currentPlayerTextLabel, 0, 0, 1, 3)
        self.currentStepLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.currentStepLabel.setMinimumSize(QtCore.QSize(0, 35))
        self.currentStepLabel.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.currentStepLabel.setFont(font)
        self.currentStepLabel.setObjectName("currentStepLabel")
        self.gridLayout_3.addWidget(self.currentStepLabel, 1, 3, 1, 3)
        self.currentPlayerLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.currentPlayerLabel.setMinimumSize(QtCore.QSize(0, 35))
        self.currentPlayerLabel.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setKerning(False)
        self.currentPlayerLabel.setFont(font)
        self.currentPlayerLabel.setAutoFillBackground(False)
        self.currentPlayerLabel.setIndent(35)
        self.currentPlayerLabel.setMargin(-30)
        self.currentPlayerLabel.setObjectName("currentPlayerLabel")
        self.gridLayout_3.addWidget(self.currentPlayerLabel, 0, 3, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.history_tableView = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.history_tableView.setObjectName("history_tableView")
        self.history_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Custom)
        self.verticalLayout_2.addWidget(self.history_tableView)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        MainWindow.setCentralWidget(self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        for x in range(1, 7):
            label = QtWidgets.QLabel(self.verticalLayoutWidget)
            label.setFont(font)
            label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
            label.setObjectName("label" + str(x))
            label.setText(str(x))
            self.boardLayout.addWidget(label, 12-x*2, 0, 2, 1)
        for x in "ABCDEF":
            label = QtWidgets.QLabel(self.verticalLayoutWidget)
            label.setFont(font)
            label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            label.setObjectName("label" + x)
            label.setText(x)
            self.boardLayout.addWidget(label, 12, 1+"ABCDEF".index(x)*2, 1, 2)

        for x in "abcdef":
            for y in range(1, 6):
                button = QtWidgets.QPushButton(self.verticalLayoutWidget)
                button.setMinimumSize(QtCore.QSize(10, 80))
                button.setMaximumSize(QtCore.QSize(10, 80))
                button.setObjectName("button" + x + str(y) + "v")
                button.setStyleSheet("background-color:#ffffff")
                button.setEnabled(False)
                self.boardLayout.addWidget(button, 12-y*2, 1+"abcdef".index(x)*2, 1, 1)
        for x in "abcde":
            for y in range(1, 7):
                button = QtWidgets.QPushButton(self.verticalLayoutWidget)
                button.setMinimumSize(QtCore.QSize(80, 10))
                button.setMaximumSize(QtCore.QSize(80, 10))
                button.setObjectName("button" + x + str(y) + "h")
                button.setStyleSheet("background-color:#ffffff")
                button.setEnabled(False)
                self.boardLayout.addWidget(button, 13-y*2, 2+"abcde".index(x)*2, 1, 1)

        for x in range(2, 11, 2):
            for y in range(2, 11, 2):
                boxLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
                boxLabel.setMinimumSize(QtCore.QSize(80, 80))
                boxLabel.setMaximumSize(QtCore.QSize(80, 80))
                font = QtGui.QFont()
                font.setPointSize(18)
                boxLabel.setFont(font)
                boxLabel.setAlignment(QtCore.Qt.AlignCenter)
                boxLabel.setObjectName("boxLabel" + str(x-1) + str(y-1))
                self.boardLayout.addWidget(boxLabel, x, y, 1, 1)
        for x in range(1, 12, 2):
            for y in range(1, 12, 2):
                pointLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
                pointLabel.setMinimumSize(QtCore.QSize(10, 10))
                pointLabel.setMaximumSize(QtCore.QSize(10, 10))
                font = QtGui.QFont()
                font.setPointSize(22)
                pointLabel.setFont(font)
                pointLabel.setAlignment(QtCore.Qt.AlignCenter)
                pointLabel.setText("•")
                self.boardLayout.addWidget(pointLabel, x, y, 1, 1)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 31))
        self.menubar.setObjectName("menubar")
        self.action00 = QtWidgets.QAction(MainWindow)
        self.action00.setObjectName("action00")
        self.action01 = QtWidgets.QAction(MainWindow)
        self.action01.setObjectName("action01")
        self.action02 = QtWidgets.QAction(MainWindow)
        self.action02.setObjectName("action02")
        self.action03 = QtWidgets.QAction(MainWindow)
        self.action03.setObjectName("action03")
        self.action10 = QtWidgets.QAction(MainWindow)
        self.action10.setObjectName("action10")
        self.action11 = QtWidgets.QAction(MainWindow)
        self.action11.setObjectName("action11")
        self.menu0 = QtWidgets.QMenu(self.menubar)
        self.menu0.setObjectName("menu0")
        self.menu0.addAction(self.action00)
        self.menu0.addAction(self.action01)
        self.menu0.addSeparator()
        self.menu0.addAction(self.action02)
        self.menu0.addAction(self.action03)
        self.menubar.addAction(self.menu0.menuAction())
        self.menu1 = QtWidgets.QMenu(self.menubar)
        self.menu1.setObjectName("menu1")
        self.menu1.addAction(self.action10)
        self.menu1.addAction(self.action11)
        self.menubar.addAction(self.menu1.menuAction())
        MainWindow.setMenuBar(self.menubar)

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "点格棋"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">•</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0055ff;\">•</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "比  分"))
        self.currentStepTextLabel.setText(_translate("MainWindow", "当前步数: "))
        self.currentPlayerTextLabel.setText(_translate("MainWindow", "当前玩家: "))
        self.currentStepLabel.setText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "历史: "))
        self.menu0.setTitle(_translate("MainWindow", "文件"))
        self.menu1.setTitle(_translate("MainWindow", "编辑"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action00.setText(_translate("MainWindow", "新游戏"))
        self.action01.setText(_translate("MainWindow", "载入游戏"))
        self.action02.setText(_translate("MainWindow", "保存游戏"))
        self.action03.setText(_translate("MainWindow", "导出标准棋谱"))
        self.action10.setText(_translate("MainWindow", "悔棋"))
        self.action11.setText(_translate("MainWindow", "恢复"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, controller, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self._controller = controller

        for x in "abcdef":
            for y in range(1, 6):
                button = self.findChild((QtWidgets.QPushButton, ), "button" + x + str(y) + "v")
                button.clicked.connect(lambda t, c=(x, str(y), "v"), b=button: self._controller.piece_button_is_clicked(c, b))
        for x in "abcde":
            for y in range(1, 7):
                button = self.findChild((QtWidgets.QPushButton, ), "button" + x + str(y) + "h")
                button.clicked.connect(lambda t, c=(x, str(y), "h"), b=button: self._controller.piece_button_is_clicked(c, b))
        self.action00.triggered.connect(lambda: self._controller.new_game())

    def set_piece_color(self, coordinate, color=None):
        piece = self.findChild((QtWidgets.QPushButton, ), "button" + coordinate[0] + coordinate[1] + coordinate[2])
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
        box = self.findChild((QtWidgets.QLabel,), "boxLabel" + coordinate[0] + coordinate[1])
        if (info == 0):
            box.setStyleSheet("background-color:#ffffff")
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
            self.currentPlayerLabel.setText("<html><head/><body><p><span style=\" color:#ff0000;\">•</span></p></body></html>")
            return
        if (color == Color.blue):
            self.currentPlayerLabel.setText("<html><head/><body><p><span style=\" color:#0055ff;\">•</span></p></body></html>")
            return
        self.currentPlayerLabel.setText("")

    def set_red_player_score(self, score):
        pass

    def set_blue_player_score(self, score):
        pass

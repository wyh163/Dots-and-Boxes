# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("点格棋")
        if (sys.platform == "linux"):
            MainWindow.resize(727, 548)
        else:
            MainWindow.resize(727, 568)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # 菜单栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 31))
        MainWindow.setMenuBar(self.menubar)
        self.menu0 = QtWidgets.QMenu(self.menubar)
        self.menu0.setObjectName("menu0")
        self.menu0.setTitle("文件")
        self.menubar.addAction(self.menu0.menuAction())
        self.menu1 = QtWidgets.QMenu(self.menubar)
        self.menu1.setObjectName("menu1")
        self.menu1.setTitle("编辑")
        self.menubar.addAction(self.menu1.menuAction())
        self.menu2 = QtWidgets.QMenu(self.menubar)
        self.menu2.setObjectName("menu2")
        self.menu2.setTitle("工具")
        self.menubar.addAction(self.menu2.menuAction())
        # 工具栏
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setWindowTitle("工具栏")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        # 状态栏
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 顶层
        self.topVerticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.topVerticalLayoutWidget.setObjectName("topVerticalLayoutWidget")
        self.topVerticalLayoutWidget.setGeometry(QtCore.QRect(8, 0, 711, 511))
        # 顶层约束
        self.topVerticalLayout = QtWidgets.QVBoxLayout(self.topVerticalLayoutWidget)
        self.topVerticalLayout.setObjectName("topVerticalLayout")
        self.topVerticalLayout.setContentsMargins(0, 0, 0, 0)
        # topLine用于分隔工具栏和中部区域
        self.topLine = QtWidgets.QFrame(self.topVerticalLayoutWidget)
        self.topLine.setObjectName("line")
        self.topLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.topLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topVerticalLayout.addWidget(self.topLine)
        # 中部区域约束
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setSpacing(0)
        self.topVerticalLayout.addLayout(self.horizontalLayout)
        # bottomLine用于分隔中部区域和状态栏
        self.bottomLine = QtWidgets.QFrame(self.topVerticalLayoutWidget)
        self.bottomLine.setObjectName("bottomLine")
        self.bottomLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.bottomLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topVerticalLayout.addWidget(self.bottomLine)

        # 菜单栏
        # 文件
        self.newGameAction = QtWidgets.QAction(self)
        self.newGameAction.setObjectName("newGameAction")
        self.newGameAction.setText("新游戏")
        self.menu0.addAction(self.newGameAction)
        self.loadGameAction = QtWidgets.QAction(self)
        self.loadGameAction.setObjectName("loadGameAction")
        self.loadGameAction.setText("载入游戏")
        self.menu0.addAction(self.loadGameAction)
        self.endGameAction = QtWidgets.QAction(self)
        self.endGameAction.setObjectName("endGameAction")
        self.endGameAction.setText("结束游戏")
        self.menu0.addAction(self.endGameAction)
        self.menu0.addSeparator()
        self.saveGameAction = QtWidgets.QAction(self)
        self.saveGameAction.setObjectName("saveGameAction")
        self.saveGameAction.setText("保存游戏")
        self.menu0.addAction(self.saveGameAction)
        # 编辑
        self.backAction = QtWidgets.QAction(self)
        self.backAction.setObjectName("backAction")
        self.backAction.setText("悔棋")
        self.menu1.addAction(self.backAction)
        self.forwardAction = QtWidgets.QAction(self)
        self.forwardAction.setObjectName("forwardAction")
        self.forwardAction.setText("恢复")
        self.menu1.addAction(self.forwardAction)
        # !!!警告！！！ 这两个按钮非常sb，在下一个版本中将删掉
        self._turnToStartAction = QtWidgets.QAction(self)
        self._turnToStartAction.setObjectName("turnToStartAction")
        self._turnToStartAction.setText("跳转到开始")
        self.menu1.addAction(self._turnToStartAction)
        self._turnToEndAction = QtWidgets.QAction(self)
        self._turnToEndAction.setObjectName("turnToEndAction")
        self._turnToEndAction.setText("跳转到最后")
        self.menu1.addAction(self._turnToEndAction)
        # 工具
        self.setRedPlayerAction = QtWidgets.QAction(self)
        self.setRedPlayerAction.setObjectName("setRedPlayerAction")
        self.setRedPlayerAction.setText("设定红方玩家")
        self.menu2.addAction(self.setRedPlayerAction)
        self.setBluePlayerAction = QtWidgets.QAction(self)
        self.setBluePlayerAction.setObjectName("setBluePlayerAction")
        self.setBluePlayerAction.setText("设定蓝方玩家")
        self.menu2.addAction(self.setBluePlayerAction)
        self.menu2.addSeparator()
        self.loadStandardRecordAction = QtWidgets.QAction(self)
        self.loadStandardRecordAction.setObjectName("loadStandardRecordAction")
        self.loadStandardRecordAction.setText("载入标准棋谱")
        self.menu2.addAction(self.loadStandardRecordAction)
        self.exportStandardRecordAction = QtWidgets.QAction(self)
        self.exportStandardRecordAction.setObjectName("exportStandardRecordAction")
        self.exportStandardRecordAction.setText("导出标准棋谱")
        self.menu2.addAction(self.exportStandardRecordAction)
        self.setPieceAnnotationAction = QtWidgets.QAction(self)
        self.setPieceAnnotationAction.setObjectName("setPieceAnnotationAction")
        self.setPieceAnnotationAction.setText("给当前步添加注释")
        self.menu2.addAction(self.setPieceAnnotationAction)

        # 工具栏

        # 中部区域
        # 棋盘约束
        self.boardLayout = QtWidgets.QGridLayout()
        self.boardLayout.setObjectName("boardLayout")
        self.boardLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.boardLayout.setContentsMargins(0, -1, -1, -1)
        self.boardLayout.setSpacing(0)
        self.horizontalLayout.addLayout(self.boardLayout)
        # middleLine用于分隔棋盘和信息区
        self.middleLine = QtWidgets.QFrame(self.topVerticalLayoutWidget)
        self.middleLine.setObjectName("middleLine")
        self.middleLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.middleLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalLayout.addWidget(self.middleLine)
        # 信息块约束，上半部分为玩家、比分等信息，下半部分为历史记录
        self.infoLayout = QtWidgets.QVBoxLayout()
        self.infoLayout.setObjectName("infoLayout")
        self.horizontalLayout.addLayout(self.infoLayout)
        # 信息区域约束
        self.topHalfLayout = QtWidgets.QGridLayout()
        self.topHalfLayout.setObjectName("topHalfLayout")
        self.infoLayout.addLayout(self.topHalfLayout)
        self.infoAreaMiddleLine = QtWidgets.QFrame(self.topVerticalLayoutWidget)
        self.infoAreaMiddleLine.setObjectName("infoAreaMiddleLine")
        self.infoAreaMiddleLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.infoAreaMiddleLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.infoLayout.addWidget(self.infoAreaMiddleLine)
        
        # 棋盘区域
        # 占位块，用于调整棋盘位置和大小
        spacerItem0 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.boardLayout.addItem(spacerItem0, 1, 12, 11, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.boardLayout.addItem(spacerItem1, 0, 1, 1, 11)
        # 坐标
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        for x in range(1, 7):
            label = QtWidgets.QLabel(self.topVerticalLayoutWidget)
            label.setObjectName("label" + str(x))
            label.setFont(font)
            label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
            label.setText(str(x))
            self.boardLayout.addWidget(label, 12-x*2, 0, 2, 1)
        for x in "ABCDEF":
            label = QtWidgets.QLabel(self.topVerticalLayoutWidget)
            label.setObjectName("label" + x)
            label.setFont(font)
            label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            label.setText(x)
            self.boardLayout.addWidget(label, 12, 1+"ABCDEF".index(x)*2, 1, 2)
        # 棋子
        font = QtGui.QFont()
        font.setPointSize(18)
        for x in "abcdef":
            for y in range(1, 6):
                button = QtWidgets.QPushButton(self.topVerticalLayoutWidget)
                button.setObjectName("button" + x + str(y) + "v")
                button.setMinimumSize(QtCore.QSize(10, 80))
                button.setMaximumSize(QtCore.QSize(10, 80))
                button.setFont(font)
                self.boardLayout.addWidget(button, 12-y*2, 1+"abcdef".index(x)*2, 1, 1)
        for x in "abcde":
            for y in range(1, 7):
                button = QtWidgets.QPushButton(self.topVerticalLayoutWidget)
                button.setObjectName("button" + x + str(y) + "h")
                button.setMinimumSize(QtCore.QSize(80, 10))
                button.setMaximumSize(QtCore.QSize(80, 10))
                button.setFont(font)
                self.boardLayout.addWidget(button, 13-y*2, 2+"abcde".index(x)*2, 1, 1)
        # 格
        for x in range(2, 11, 2):
            for y in range(2, 11, 2):
                boxLabel = QtWidgets.QLabel(self.topVerticalLayoutWidget)
                boxLabel.setMinimumSize(QtCore.QSize(80, 80))
                boxLabel.setMaximumSize(QtCore.QSize(80, 80))
                font = QtGui.QFont()
                font.setPointSize(18)
                boxLabel.setFont(font)
                boxLabel.setAlignment(QtCore.Qt.AlignCenter)
                boxLabel.setObjectName("boxLabel" + str(x-1) + str(y-1))
                self.boardLayout.addWidget(boxLabel, x, y, 1, 1)
        # 点
        for x in range(1, 12, 2):
            for y in range(1, 12, 2):
                pointLabel = QtWidgets.QLabel(self.topVerticalLayoutWidget)
                pointLabel.setMinimumSize(QtCore.QSize(10, 10))
                pointLabel.setMaximumSize(QtCore.QSize(10, 10))
                font = QtGui.QFont()
                font.setPointSize(22)
                pointLabel.setFont(font)
                pointLabel.setAlignment(QtCore.Qt.AlignCenter)
                pointLabel.setText("•")
                self.boardLayout.addWidget(pointLabel, x, y, 1, 1)

        # 信息区域
        # 当前玩家
        self.currentPlayerTextLabel = QtWidgets.QLabel(self.topVerticalLayoutWidget)
        self.currentPlayerTextLabel.setObjectName("currentPlayerTextLabel")
        font13 = QtGui.QFont()
        font13.setPointSize(13)
        self.currentPlayerTextLabel.setFont(font13)
        self.currentPlayerTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.currentPlayerTextLabel.setText("当前玩家: ")
        self.topHalfLayout.addWidget(self.currentPlayerTextLabel, 0, 0, 1, 3)
        self.currentPlayerLabel = QtWidgets.QLabel(self.topVerticalLayoutWidget)
        self.currentPlayerLabel.setObjectName("currentPlayerLabel")
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setKerning(False)
        self.currentPlayerLabel.setFont(font)
        self.currentPlayerLabel.setAutoFillBackground(False)
        if (sys.platform == "linux"):
            self.currentPlayerLabel.setIndent(35)
            self.currentPlayerLabel.setMargin(-30)
        else:
            self.currentPlayerLabel.setFixedHeight(40)
            self.currentPlayerLabel.setMargin(-7)
        self.topHalfLayout.addWidget(self.currentPlayerLabel, 0, 3, 1, 3)
        # 当前步数
        self.currentStepTextLabel = QtWidgets.QLabel(self.topVerticalLayoutWidget)
        self.currentStepTextLabel.setObjectName("currentStepTextLabel")
        self.currentStepTextLabel.setFont(font13)
        self.currentStepTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.currentStepTextLabel.setText("当前步数: ")
        self.topHalfLayout.addWidget(self.currentStepTextLabel, 1, 0, 1, 3)
        self.currentStepLabel = QtWidgets.QLabel(self.topVerticalLayoutWidget)
        self.currentStepLabel.setObjectName("currentStepLabel")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.currentStepLabel.setFont(font)
        self.currentStepLabel.setText("0")
        if (sys.platform != "linux"):
            self.currentStepLabel.setFixedHeight(40)
        self.topHalfLayout.addWidget(self.currentStepLabel, 1, 3, 1, 3)
        # 比分
        scoreSpacerItem0 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topHalfLayout.addItem(scoreSpacerItem0, 2, 5, 2, 1)
        scoreSpacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topHalfLayout.addItem(scoreSpacerItem1, 2, 0, 2, 1)
        self.scoreTextLabel = QtWidgets.QLabel(self.topVerticalLayoutWidget)
        self.scoreTextLabel.setObjectName("scoreTextLabel")
        self.scoreTextLabel.setFont(font13)
        self.scoreTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreTextLabel.setText("比  分")
        self.topHalfLayout.addWidget(self.scoreTextLabel, 2, 1, 1, 4)
        # 双方分数
        self.redScoreTextLabel = QtWidgets.QLabel(self.topVerticalLayoutWidget)
        self.redScoreTextLabel.setObjectName("redScoreTextLabel")
        self.redScoreTextLabel.setMinimumSize(QtCore.QSize(25, 30))
        self.redScoreTextLabel.setMaximumSize(QtCore.QSize(25, 30))
        font38 = QtGui.QFont()
        font38.setPointSize(38)
        self.redScoreTextLabel.setFont(font38)
        self.redScoreTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.redScoreTextLabel.setText("<html><head/><body><p><span style=\" color:#ff0000;\">•</span></p></body></html>")
        if (sys.platform == "linux"):
            self.redScoreTextLabel.setIndent(17)
            self.redScoreTextLabel.setMargin(-16)
        else:
            self.redScoreTextLabel.setIndent(7)
            self.redScoreTextLabel.setMargin(-9)
        self.topHalfLayout.addWidget(self.redScoreTextLabel, 3, 1, 1, 1)
        self.blueScoreTextLabel = QtWidgets.QLabel(self.topVerticalLayoutWidget)
        self.blueScoreTextLabel.setObjectName("blueScoreTextLabel")
        self.blueScoreTextLabel.setMinimumSize(QtCore.QSize(25, 30))
        self.blueScoreTextLabel.setMaximumSize(QtCore.QSize(25, 30))
        self.blueScoreTextLabel.setFont(font38)
        self.blueScoreTextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.blueScoreTextLabel.setText("<html><head/><body><p><span style=\" color:#0055ff;\">•</span></p></body></html>")
        if (sys.platform == "linux"):
            self.blueScoreTextLabel.setIndent(17)
            self.blueScoreTextLabel.setMargin(-16)
        else:
            self.blueScoreTextLabel.setIndent(7)
            self.blueScoreTextLabel.setMargin(-9)
        self.topHalfLayout.addWidget(self.blueScoreTextLabel, 3, 3, 1, 1)
        self.redScoreNumber = QtWidgets.QLCDNumber(self.topVerticalLayoutWidget)
        self.redScoreNumber.setObjectName("redScoreNumber")
        self.redScoreNumber.setMinimumSize(QtCore.QSize(40, 25))
        self.redScoreNumber.setMaximumSize(QtCore.QSize(40, 25))
        self.redScoreNumber.setDigitCount(2)
        self.redScoreNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.redScoreNumber.setStyleSheet("color: #64ff32; background-color: #303030")
        self.topHalfLayout.addWidget(self.redScoreNumber, 3, 2, 1, 1)
        self.blueScoreNumber = QtWidgets.QLCDNumber(self.topVerticalLayoutWidget)
        self.blueScoreNumber.setObjectName("blueScoreNumber")
        self.blueScoreNumber.setMinimumSize(QtCore.QSize(40, 25))
        self.blueScoreNumber.setMaximumSize(QtCore.QSize(40, 25))
        self.blueScoreNumber.setDigitCount(2)
        self.blueScoreNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.blueScoreNumber.setStyleSheet("color: #64ff32; background-color: #303030")
        self.topHalfLayout.addWidget(self.blueScoreNumber, 3, 4, 1, 1)
        # 历史信息
        self.historyTextLabel = QtWidgets.QLabel(self.topVerticalLayoutWidget)
        self.historyTextLabel.setObjectName("historyTextLabel")
        self.historyTextLabel.setText("历史: ")
        self.infoLayout.addWidget(self.historyTextLabel)
        self.historyTableView = QtWidgets.QTableView(self.topVerticalLayoutWidget)
        self.historyTableView.setObjectName("historyTableView")
        self.historyTableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Custom)
        self.infoLayout.addWidget(self.historyTableView)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


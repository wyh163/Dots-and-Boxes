# -*- coding: UTF-8 -*-
from DotsAndBoxes.main_window_controller import MainWindowController
import sys
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window_controller = MainWindowController()
    main_window_controller.window.show()
    sys.exit(app.exec_())


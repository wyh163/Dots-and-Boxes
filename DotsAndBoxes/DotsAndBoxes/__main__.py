# -*- coding: UTF-8 -*-
import sys

from DotsAndBoxes.main_window_controller import MainWindowController
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window_controller = MainWindowController()
    main_window_controller.window.show()
    sys.exit(app.exec_())


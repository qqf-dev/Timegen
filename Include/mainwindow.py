# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    def __init__(self):
        self.ui = QUiLoader().load('UI/mainwindow.ui')
        QMainWindow.__init__(self)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.ui.show()
    sys.exit(app.exec_())

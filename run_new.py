from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout, QPushButton,
                             QMainWindow, QLabel, QToolBar, QAction, QStatusBar)
from PyQt5.QtGui import QIcon
import sys
from PyQt5 import QtCore

class App(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self.setWindowTitle("My Awesome App")
        self.title = 'Liquidctl'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        label = QLabel("Liquidctl")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.setCentralWidget(label)
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QtCore.QSize(16,16))
        self.addToolBar(toolbar)

        # Button for each Tab
          # First Button
        button_action = QAction(QIcon("icon.jpg"), "Settings", self)
        # button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
          # Second Button
        button_action1 = QAction(QIcon("icon.jpg"), "RGB", self)
        button_action1.setCheckable(True)
        toolbar.addAction(button_action1)

        self.setStatusBar(QStatusBar(self))
        self.initUI()


    def onMyToolBarButtonClick(self, s):
        print("click", s)


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

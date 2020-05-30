'''
Main file to run the GUI program
'''
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QTabWidget,
                             QVBoxLayout, QPushButton, QMainWindow, QLabel,
                             QToolBar, QAction, QStatusBar, QSystemTrayIcon,
                             QMenu, QCheckBox, QColorDialog)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
import sys
import logging

from settings import load_settings, change_setting

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Liquidctl'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.layout = QVBoxLayout(self)

        # Initialize Tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "RGB")
        self.tabs.addTab(self.tab2, "Pumps")
        self.tabs.addTab(self.tab3, "Settings")

        # Create First Tab
        self.tab1.layout = QVBoxLayout(self)
        pushbutton1 = QPushButton("Color")
        self.tab1.layout.addWidget(pushbutton1)
        pushbutton1.clicked.connect(lambda: self.showColorDialog(pushbutton1))

        pushbutton2 = QPushButton("Color")
        self.tab1.layout.addWidget(pushbutton2)
        pushbutton2.clicked.connect(lambda: self.showColorDialog(pushbutton2))

        # color = QColorDialog()
        # self.tab1.layout.addWidget(color)
        pushbutton3 = QPushButton('Dialog', self)
        self.tab1.layout.addWidget(pushbutton3)
        pushbutton3.clicked.connect(lambda: self.showColorDialog(pushbutton3))
        self.tab1.setLayout(self.tab1.layout)

        # Create the second tab

        # Create the Settings Tab
        self.tab3.layout = QVBoxLayout(self)
        self.settings = load_settings()

        self.checkbox1 = QCheckBox("Run at startup")
        self.checkbox1.setChecked(bool(self.settings["RunAtStartup"]))
        self.tab3.layout.addWidget(self.checkbox1)
        self.checkbox1.stateChanged.connect(lambda: change_setting("RunAtStartup"))

        self.checkbox2 = QCheckBox("Minimize to tray on close")
        self.checkbox2.setChecked(bool(self.settings["MinimizeToTray"]))
        self.tab3.layout.addWidget(self.checkbox2)
        self.checkbox2.stateChanged.connect(lambda: change_setting("MinimizeToTray"))

        self.checkbox3 = QCheckBox("Check for updates automatically")
        self.checkbox3.setChecked(bool(self.settings["KeepUpdated"]))
        self.tab3.layout.addWidget(self.checkbox3)
        self.checkbox3.stateChanged.connect(lambda: change_setting("KeepUpdated"))

        self.checkbox4 = QCheckBox("Report Errors")
        self.checkbox4.setChecked(bool(self.settings["ReportBugs"]))
        self.tab3.layout.addWidget(self.checkbox4)
        self.checkbox4.stateChanged.connect(lambda: change_setting("ReportBugs"))

        self.tab3.setLayout(self.tab3.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        # Attribute for if a system tray can be used
        self.has_systray = QSystemTrayIcon.isSystemTrayAvailable()

        self.initUI()

    def set_sys_tray_icon(self):
        if self.has_systray:
            icon = QSystemTrayIcon(QIcon("icon.jpg"), self)
            icon_menu = QMenu('Test')
            icon_menu.addAction('Foo')
            icon_menu.addSeparator()
            icon_menu.addAction('Exit')
            icon.setContextMenu(icon_menu)
            icon.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.set_sys_tray_icon()
        self.show()


    def showColorDialog(self, button):
        color = QColorDialog.getColor()

        if color.isValid():
            button.setStyleSheet('QWidget { background-color: %s }'
                                   % color.name())
            logger.info("Button has a color")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

'''
Main file to run the GUI program
'''
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QTabWidget,
                             QVBoxLayout, QPushButton, QMainWindow, QLabel,
                             QToolBar, QAction, QStatusBar, QSystemTrayIcon,
                             QMenu, QCheckBox, QColorDialog, QDial, QLabel,
                             QBoxLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtCore import Qt
import sys
import logging
import random
import functools

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

        # Create RGB Tab
        self.tab1.layout = QVBoxLayout(self)
        devices = self.get_devices()
        for device in devices:
            box_layout = QVBoxLayout()
            box_layout.addWidget(QLabel(device))
            push_button = QPushButton("")
            push_button.clicked.connect(lambda checked, btn=push_button: self.add_color_dialog(btn))
            box_layout.addWidget(push_button)
            # Add other stuff here for each device
            self.tab1.layout.addLayout(box_layout)
        self.tab1.setLayout(self.tab1.layout)


        # Create the Fan Speed and Pump Speed tab
        self.tab2.layout = QVBoxLayout(self)
        chartView = QChartView()
        chart = chartView.chart()
        minSize = 0.0
        maxSize = 1.0
        donutCount = 1
        m_donuts = []
        donut = QPieSeries()
        sliceCount = 2
        for j in range(sliceCount):
            value = 90
            slice = QPieSlice(str(value), value)
            slice.angleSpan = 90
            donut.append(slice)
            donut.setHoleSize(0.9)
            donut.setPieSize(minSize + (1 + 1) * (maxSize - minSize) / donutCount)
            m_donuts.append(donut)
            chartView.chart().addSeries(donut)
        donut.setPieStartAngle(240)
        donut.setPieEndAngle(90)
        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(chartView, 1)
        chartView.show()
        self.tab2.setLayout(mainLayout)


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

    def add_color_dialog(self, button):
        color = QColorDialog.getColor()

        if color.isValid():
            color_hex = color.name()

            button.setStyleSheet('background-color: %s' % color_hex)
            logger.info(" %s has been set to color: %s" % (button, color_hex))

    def get_devices(self):
        from liquidctl.driver import find_liquidctl_devices
        devices = []
        for device in find_liquidctl_devices():
            devices.append(device.description.split("(")[0])
            logger.info(" Found: %s" % device)
        return devices

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

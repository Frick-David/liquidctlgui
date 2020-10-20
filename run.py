'''
Main file to run the GUI program
'''
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QTabWidget,
                             QVBoxLayout, QPushButton, QMainWindow, QLabel,
                             QToolBar, QAction, QStatusBar, QSystemTrayIcon,
                             QMenu, QCheckBox)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
import sys

from settings import load_settings, change_setting

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
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tab1.layout.addWidget(self.pushButton1)
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


from PyQt5 import QtCore, QtGui, QtWidgets


class TabBar(QtWidgets.QTabBar):

    def tabSizeHint(self, index):
        s = QtWidgets.QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        opt = QtWidgets.QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt);
            painter.restore()



class TabWidget(QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTabWidget.__init__(self, *args, **kwargs)
        self.setTabBar(TabBar(self))
        self.setTabPosition(QtWidgets.QTabWidget.West)


class ProxyStyle(QtWidgets.QProxyStyle):
    def drawControl(self, element, opt, painter, widget):
        if element == QtWidgets.QStyle.CE_TabBarTabLabel:
            ic = self.pixelMetric(QtWidgets.QStyle.PM_TabBarIconSize)
            r = QtCore.QRect(opt.rect)
            w =  0 if opt.icon.isNull() else opt.rect.width() + self.pixelMetric(QtWidgets.QStyle.PM_TabBarIconSize)
            r.setHeight(opt.fontMetrics.width(opt.text) + w)
            r.moveBottom(opt.rect.bottom())
            opt.rect = r
        QtWidgets.QProxyStyle.drawControl(self, element, opt, painter, widget)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.setStyle(ProxyStyle())
    w = TabWidget()
    w.setStyleSheet("border: none;")

    # RGB Widget
    rgb_widget = QtWidgets.QWidget()
    rgb_widget.layout = QVBoxLayout()
    rgb_widget.label = QLabel("Placeholder Text")
    rgb_widget.layout.addWidget(rgb_widget.label)
    rgb_widget.setWindowTitle("Fan Control")
    rgb_widget.setLayout(rgb_widget.layout)
    # Add our RGB Widget to the main window
    w.addTab(rgb_widget, QtGui.QIcon("icons/rgb-lights.png"), None)         # RGB Tab

    # Fans Tab
    fans_widget = QtWidgets.QWidget()
    fans_widget.layout = QVBoxLayout()
    fans_widget.label = QLabel("Placeholder Text")
    fans_widget.layout.addWidget(fans_widget.label)
    fans_widget.setWindowTitle("Fan Control")
    fans_widget.setLayout(fans_widget.layout)
    # Add our fan widget to the main window
    w.addTab(fans_widget, QtGui.QIcon("icons/fans.png"), None)               # Fans tab

    # Settings Tab
    settings_widget = QtWidgets.QWidget()
    settings_widget.layout = QVBoxLayout()
    settings_widget.label = QLabel("Placeholder Text")
    settings_widget.layout.addWidget(settings_widget.label)
    settings_widget.setWindowTitle("Settings")
    settings_widget.setLayout(settings_widget.layout)

    # Create the Settings Tab
    settings_widget.settings = load_settings()  # Incorporate this
    settings_widget.checkbox1 = QCheckBox("Run at startup")
    settings_widget.checkbox1.setChecked(bool(settings_widget.settings["RunAtStartup"]))
    settings_widget.layout.addWidget(settings_widget.checkbox1)
    settings_widget.checkbox1.stateChanged.connect(lambda: change_setting("RunAtStartup"))

    settings_widget.checkbox2 = QCheckBox("Minimize to tray on close")
    settings_widget.checkbox2.setChecked(bool(settings_widget.settings["MinimizeToTray"]))
    settings_widget.layout.addWidget(settings_widget.checkbox2)
    settings_widget.checkbox2.stateChanged.connect(lambda: change_setting("MinimizeToTray"))

    settings_widget.checkbox3 = QCheckBox("Check for updates automatically")
    settings_widget.checkbox3.setChecked(bool(settings_widget.settings["KeepUpdated"]))
    settings_widget.layout.addWidget(settings_widget.checkbox3)
    settings_widget.checkbox3.stateChanged.connect(lambda: change_setting("KeepUpdated"))

    settings_widget.checkbox4 = QCheckBox("Report Errors")
    settings_widget.checkbox4.setChecked(bool(settings_widget.settings["ReportBugs"]))
    settings_widget.layout.addWidget(settings_widget.checkbox4)
    settings_widget.checkbox4.stateChanged.connect(lambda: change_setting("ReportBugs"))

    # Add our settings widget to the main window
    w.addTab(settings_widget, QtGui.QIcon("icons/settings.jpg"), None)           # Settings Tab


    w.resize(640, 480)
    w.show()

    sys.exit(app.exec_())

#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())



#
# # See if we can make the button border more or less invisible
# # This looks better than the tab type things
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot
#
# class App(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 button - pythonspot.com'
#         self.left = 10
#         self.top = 10
#         self.width = 320
#         self.height = 200
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#         button = QPushButton('PyQt5 button', self)
#         button.setToolTip('This is an example button')
#         button.setStyleSheet("border: none;")
#         button.move(100,70)
#         button.clicked.connect(self.on_click)
#
#         self.show()
#
#     @pyqtSlot()
#     def on_click(self):
#         print('PyQt5 button click')
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())

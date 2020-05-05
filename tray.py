from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QLabel
from PyQt5.QtGui import QIcon


app = QApplication([])
has_systray = QSystemTrayIcon.isSystemTrayAvailable()
label = QLabel(f'System tray available: {has_systray}')
label.show()

icon_menu = QMenu('Test')
icon_menu.addAction('Foo')
icon_menu.addSeparator()
icon_menu.addAction('Bar')

icon = QSystemTrayIcon(QIcon("icon.jpg"), app)
icon.setContextMenu(icon_menu)
icon.show()

app.exec_()

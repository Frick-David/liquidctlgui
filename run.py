'''
Main file to run the GUI program
'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon

# Will want to import settings here

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

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

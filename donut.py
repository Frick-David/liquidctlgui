# from: https://doc.qt.io/qt-5/qtcharts-nesteddonuts-example.html
import functools
import random

from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Widget(QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(800, 600)

        self.m_donuts = []

        self.chartView = QChartView()
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chart = self.chartView.chart()
        self.chart.legend().setVisible(False)
        self.chart.setTitle("Nested donuts demo")
        self.chart.setAnimationOptions(QChart.AllAnimations)

        minSize = 0.1
        maxSize = 0.9
        donutCount = 5

        for i in range(donutCount):
            donut = QPieSeries()
            sliceCount = random.randrange(3, 6)
            for j in range(sliceCount):
                value = random.randrange(100, 200)
                slice_ = QPieSlice(str(value), value)
                slice_.setLabelVisible(True)
                slice_.setLabelColor(Qt.white)
                slice_.setLabelPosition(QPieSlice.LabelInsideTangential)
                slice_.hovered[bool].connect(functools.partial(self.explodeSlice, slice_=slice_))
                donut.append(slice_)
                donut.setHoleSize(minSize + i * (maxSize - minSize) / donutCount)
                donut.setPieSize(minSize + (i + 1) * (maxSize - minSize) / donutCount)

            self.m_donuts.append(donut)
            self.chartView.chart().addSeries(donut)


        # create main layout
        self.mainLayout = QGridLayout(self)
        self.mainLayout.addWidget(self.chartView, 1, 1)
        self.chartView.show()
        self.setLayout(self.mainLayout)

        self.updateTimer = QTimer(self)
        self.updateTimer.timeout.connect(self.updateRotation)
        self.updateTimer.start(1250)


    def updateRotation(self):
        for donut in self.m_donuts:
            phaseShift =  random.randrange(-50, 100)
            donut.setPieStartAngle(donut.pieStartAngle() + phaseShift)
            donut.setPieEndAngle(donut.pieEndAngle() + phaseShift)


    def explodeSlice(self, exploded, slice_):
        if exploded:
            self.updateTimer.stop()
            sliceStartAngle = slice_.startAngle()
            sliceEndAngle = slice_.startAngle() + slice_.angleSpan()

            donut = slice_.series()
            seriesIndex = self.m_donuts.index(donut)
            for i in range(seriesIndex + 1, len(self.m_donuts)):
                self.m_donuts[i].setPieStartAngle(sliceEndAngle)
                self.m_donuts[i].setPieEndAngle(360 + sliceStartAngle)
        else:
            for donut in self.m_donuts:
                donut.setPieStartAngle(0)
                donut.setPieEndAngle(360)
            self.updateTimer.start()
        slice_.setExploded(exploded)


a = QApplication([])
w = Widget()
w.show()
a.exec_()

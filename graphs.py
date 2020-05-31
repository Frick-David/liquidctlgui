import pyqtgraph as pg
import pyqtgraph.exporters

# define the data
title = "pyqtgraph plot"
y = [2,4,6,8,10,12,14,16,18,20]
x = range(0,10)

# create plot
plt = pg.plot(x, y, title=title, pen='r')
plt.showGrid(x=False,y=False)


if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()

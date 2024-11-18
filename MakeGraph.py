import GetData
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        time = GetData.unix_time
        #data_1 = GetData.close_price
        data_2 = GetData.mid_price

        #Add Title
        self.graphWidget.setTitle(GetData.stock_code+', '+GetData.exchange_code, color="w", size="20pt")
        #Add Axis Labels
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Price", **styles)
        self.graphWidget.setLabel("bottom", "Time (msec)", **styles)
        #Add grid
        self.graphWidget.showGrid(x=True, y=True)
        #Set Range
        self.graphWidget.setXRange(min(GetData.unix_time), max(GetData.unix_time), padding=0)
        self.graphWidget.setYRange(min(GetData.open_price), max(GetData.close_price), padding=0)
        #Add plot
        #self.plot(time, data_1, "Close", 'r')
        self.plot(time, data_2, "Mid_price", 'b')

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='o', symbolSize=5, symbolBrush=(color))

def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec()

if __name__ == '__main__':
    main()
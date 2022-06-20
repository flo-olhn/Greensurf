# This Python file uses the following encoding: utf-8
from enum import auto
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore
from ui_mainwindow import Ui_MainWindow
import psutil
import pyqtgraph as pg


class NetworkTraffic():

    def __init__(self):
        self.starting_values = psutil.net_io_counters()
        self.starting_bytes_nb = self.starting_values[0] + self.starting_values[1]
        self.co2eq = 0

    def networkTrafficEmissions(self, start_val):
        values = psutil.net_io_counters()
        bytes_sent = values[0]
        bytes_received = values[1]
        total_bytes = bytes_sent + bytes_received
        # DEBUG
        # print(self.co2eq)
        self.co2eq += (((total_bytes - self.starting_bytes_nb) * 1.52E-10) * 0.055)
        self.starting_bytes_nb = total_bytes
        return self.co2eq


class MainWindow(QMainWindow):
    """
    background color: #1A1E26
    background color darker: #101217
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet("background-color: #101217;")

        # Initialisation obj NetworkTraffic
        self.net_traffic = NetworkTraffic()

        self.time_axis = [0 for i in range(86400)]
        self.total = [0 for i in range(86400)]

        self.ui.startButton.clicked.connect(self.start)
        self.ui.stopButton.clicked.connect(self.stop)
        self.ui.networkGraph.setBackground('#101217')
        self.ui.hardwareGraph.setBackground('#101217')

        self.ui.networkGraph.showGrid(x=True, y=True, alpha=0.1)
        self.ui.hardwareGraph.showGrid(x=True, y=True, alpha=0.1)
        self.ui.hardwareGraph.setBackground('#101217')
        self.pen = pg.mkPen(color=(94, 255, 125))

        self.data_line = self.ui.networkGraph.plot([],[], fillLevel = min(self.total), brush=pg.mkBrush(110, 255, 165, 10), pen=self.pen)
        self.data_line2 = self.ui.hardwareGraph.plot([], [], pen=self.pen)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)

        self.timer.timeout.connect(self.updatePlotData)

    def start(self):
        self.net_traffic = NetworkTraffic()
        self.time_axis = [0 for i in range(86400)]
        self.total = [0 for i in range(86400)]
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def updatePlotData(self):
        self.time_axis = self.time_axis[1:]
        self.time_axis.append(self.time_axis[-1] + 1)
        self.total = self.total[1:]
        if (self.time_axis[-1] + 1) % 3600 == 0:
            self.ui.networkGraph.setXRange(self.time_axis[-1], self.time_axis[-1] + 3600)
            self.ui.hardwareGraph.setXRange(self.time_axis[-1], self.time_axis[-1] + 3600)
        m = max(self.total)
        self.total.append(self.net_traffic.networkTrafficEmissions(self.net_traffic.starting_bytes_nb))
        if (m < max(self.total)) and (self.time_axis[-1] + 1 > 3600): 
            self.ui.networkGraph.setYRange(self.total[-3600],max(self.total))
            self.ui.hardwareGraph.setYRange(self.total[-3600],max(self.total))
        self.data_line.setData(self.time_axis, self.total)
        self.data_line2.setData(self.time_axis, self.total)

    """
    def networkTrafficEmissions(self):
        values = psutil.net_io_counters()
        bytes_sent = values[0]
        bytes_received = values[1]
        total_bytes = bytes_sent + bytes_received
        total = (total_bytes * 1.52E-10) * 0.057
        return total
    """


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

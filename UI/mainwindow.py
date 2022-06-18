# This Python file uses the following encoding: utf-8
from enum import auto
import sys
from turtle import pen

from PySide6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore
from ui_mainwindow import Ui_MainWindow
import psutil
import pyqtgraph as pg


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.time_axis = [0 for i in range(86400)] 
        ini = self.networkTrafficEmissions()
        self.total = [ini for i in range(86400)]
        self.ui.networkFrame.addWidget(self.ui.networkGraph)
        self.ui.startButton.clicked.connect(self.start)
        self.ui.stopButton.clicked.connect(self.stop)
        self.ui.networkGraph.setBackground('w')
        pen = pg.mkPen(color=(0, 255, 0))
        self.data_line = self.ui.networkGraph.plot([], [], pen=pen)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot_data)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def update_plot_data(self):
        self.time_axis = self.time_axis[1:]
        self.time_axis.append(self.time_axis[-1] + 1)
        self.total = self.total[1:]
        if (self.time_axis[-1] + 1) % 60 == 0:
            self.ui.networkGraph.setXRange(self.time_axis[-1], self.time_axis[-1] + 60)
        m = max(self.total)
        self.total.append(self.networkTrafficEmissions())
        if (m < max(self.total)) and (self.time_axis[-1] + 1 > 60): 
            self.ui.networkGraph.setYRange(self.total[-60],max(self.total))
        self.data_line.setData(self.time_axis, self.total)

    def networkTrafficEmissions(self):
        values = psutil.net_io_counters()
        bytes_sent = values[0]
        bytes_received = values[1]
        total_bytes = bytes_sent + bytes_received
        total = (total_bytes * 1.52E-10) * 0.057
        return total


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

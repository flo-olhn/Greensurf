# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout
from ui_mainwindow import Ui_MainWindow
import numpy as np
import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

"""
Problem:
    - conflict between matplotlib and QMainWindow show() method.
"""


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.time_axis = []
        self.total = []
        self.ui.networkFrame.addWidget(FigureCanvas(self.p()))
        self.setLayout(self.ui.networkFrame)
        self.show()
        self.ui.startButton.clicked.connect(self.start)

    def start(self):
        self.time_axis = []
        self.total = []

    def networkTrafficEmissions(self):
        values = psutil.net_io_counters()
        bytes_sent = values[0]
        bytes_received = values[1]
        total_bytes = bytes_sent + bytes_received
        total = (total_bytes * 1.52E-10) * 0.057
        return total

    def animate(self, i):
        self.time_axis.append(i)
        self.total.append(round(self.networkTrafficEmissions(), 10))
        avg =  [np.mean(self.total)] * len(self.total)
        plt.cla()
        plt.ylabel("GHG Emission - kgCO2eq")
        plt.xticks([])
        plt.yscale("log")
        plt.plot(self.time_axis, self.total, color='#46DB96', linewidth=0.5)
        plt.fill_between(self.time_axis, self.total, color='#46DB96', alpha=0.2)
        plt.plot(self.time_axis, avg, color='blue', linewidth=0.5, alpha=0.4, ls='--', )
        # Uncomment the line below to display average GHG Emission value on chart
        # plt.annotate(str(avg[0]), xy=(avg[0], avg[0]))


    def p(self):
        ani = FuncAnimation(plt.gcf(), self.animate, interval=1000)
        plt.show()
        # return ani


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    # widget.show()
    sys.exit(app.exec())

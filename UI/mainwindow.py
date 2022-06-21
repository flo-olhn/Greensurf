# This Python file uses the following encoding: utf-8
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

    def emissions(self):
        values = psutil.net_io_counters()
        bytes_sent = values[0]
        bytes_received = values[1]
        bytes_total = bytes_sent + bytes_received
        self.co2eq += ((bytes_total - self.starting_bytes_nb) * 1.52E-10) * 0.055
        self.starting_bytes_nb = bytes_total
        return self.co2eq


class Graph():

    def __init__(self) -> None:
        self.x_values = [0 for i in range(86400)]
        self.y_values = [0 for i in range(86400)]
        self.pen = pg.mkPen(color=(94, 255, 125))
        self.data_line = []
        self.pen = pg.mkPen(color=(94, 255, 125))
        # self.data_line = MainWindow.ui.networkGraph.plot([],[], fillLevel = min(self.y_values), brush=pg.mkBrush(110, 255, 165, 10), pen=self.pen)

    def updatePlotData(self, graph_ui, graph_type):
        self.x_values = self.x_values[1:]
        self.x_values.append(self.x_values[-1] + 1)
        self.y_values = self.y_values[1:]
        if (self.x_values[-1] + 1) % 3600 == 0:
            graph_ui.setXRange(self.x_values[-1], self.x_values[-1] + 3600)
            #self.ui.hardwareGraph.setXRange(self.x_values[-1], self.x_values[-1] + 3600)
        m = max(self.y_values)
    
        # modification to do -> what if i need to plot on hardware graph instead???
        self.y_values.append(graph_type.emissions())


        if (m < max(self.y_values)) and (self.x_values[-1] + 1 > 3600): 
            graph_ui.setYRange(self.y_values[-3600],max(self.y_values))
            #self.ui.hardwareGraph.setYRange(self.y_values[-3600],max(self.y_values))
        self.data_line.setData(self.x_values, self.y_values)
        #self.data_line2.setData(self.x_values, self.y_values)


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

        # Initialisation obj NetworkTraffic and Graph
        self.net_traffic = NetworkTraffic()
        self.net_graph = Graph()

        self.ui.startButton.clicked.connect(self.start)
        self.ui.stopButton.clicked.connect(self.stop)
        self.ui.networkGraph.setBackground('#101217')
        self.ui.hardwareGraph.setBackground('#101217')

        self.ui.networkGraph.showGrid(x=True, y=True, alpha=0.1)
        self.ui.hardwareGraph.showGrid(x=True, y=True, alpha=0.1)
        self.ui.hardwareGraph.setBackground('#101217')
        
        self.pen = pg.mkPen(color=(94, 255, 125))
        self.net_graph.data_line = self.ui.networkGraph.plot([],[], fillLevel = min(self.net_graph.y_values), brush=pg.mkBrush(110, 255, 165, 10), pen=self.net_graph.pen)
        self.data_line2 = self.ui.hardwareGraph.plot([], [], pen=self.pen)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)

        self.timer.timeout.connect(lambda: self.net_graph.updatePlotData(self.ui.networkGraph, self.net_traffic))
        #self.timer.timeout.connect(self.updatePlotData)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()
        self.net_graph.x_values = [0 for _ in range(86400)]
        self.net_graph.y_values = [0 for _ in range(86400)]
    

if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

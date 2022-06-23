# This Python file uses the following encoding: utf-8
import sys
from datetime import timedelta
from PySide6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore
from PySide6.QtGui import QIcon
from ui_mainwindow import Ui_MainWindow
import psutil
import pyqtgraph as pg
from emissions_tracker import EmissionsTracker




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
        

class HardwareEmission():

    def __init__(self):
        self.hardware_tracker = EmissionsTracker()
        self.val = 0

    def emissions(self):
        self.hardware_tracker.start()
        self.val = self.hardware_tracker.stop()
        return self.val


class Graph():

    def __init__(self) -> None:
        self.x_values = [0 for _ in range(86400)]
        self.y_values = [0 for _ in range(86400)]
        self.pen = pg.mkPen(color=(94, 255, 125))
        self.data_line = []
        self.data_line2 = []
        self.pen = pg.mkPen(color=(94, 255, 125))
        # print(cpuname(), gpuname())

    def updatePlotData(self, graph_ui, graph_type):
        self.x_values = self.x_values[1:]
        self.x_values.append(self.x_values[-1] + 1)
        self.y_values = self.y_values[1:]
        if (self.x_values[-1] + 1) % 3600 == 0:
            graph_ui.setXRange(self.x_values[-1], self.x_values[-1] + 3600)
        m = max(self.y_values)
        self.y_values.append(graph_type.emissions())
        if (m < max(self.y_values)) and (self.x_values[-1] + 1 > 3600): 
            graph_ui.setYRange(self.y_values[-3600],max(self.y_values))
        self.data_line.setData(self.x_values, self.y_values)
        #emission_fun()


class MainWindow(QMainWindow):
    """
    background color: #1A1E26
    background color darker: #101217
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("C:/Users/ouilh/OneDrive/Documents/Projet_E3/Greensurf/UI/assets/greensurf_icon.ico"))

        # Initialisation obj NetworkTraffic and Graph
        self.net_traffic = NetworkTraffic()
        self.hardware = HardwareEmission()
        self.net_graph = Graph()
        self.hardware_graph = Graph()

        self.ui.startButton.clicked.connect(self.start)
        self.ui.stopButton.clicked.connect(self.stop)
        self.ui.networkGraph.setBackground('#101217')
        self.ui.hardwareGraph.setBackground('#101217')

        self.ui.networkGraph.showGrid(x=True, y=True, alpha=0.1)
        self.ui.hardwareGraph.showGrid(x=True, y=True, alpha=0.1)
        self.ui.hardwareGraph.setBackground('#101217')
        self.ui.stopButton.setEnabled(False)
        
        self.pen = pg.mkPen(color=(94, 255, 125))
        self.net_graph.data_line = self.ui.networkGraph.plot([],[], fillLevel = min(self.net_graph.y_values), brush=pg.mkBrush(110, 255, 165, 10), pen=self.net_graph.pen)

        self.hardware_graph.data_line = self.ui.hardwareGraph.plot([],[], fillLevel = min(self.hardware_graph.y_values), brush=pg.mkBrush(110, 255, 165, 10), pen=self.hardware_graph.pen)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)

        self.timer.timeout.connect(lambda: self.net_graph.updatePlotData(self.ui.networkGraph, self.net_traffic))
        self.timer.timeout.connect(lambda: self.hardware_graph.updatePlotData(self.ui.hardwareGraph, self.hardware))
        self.timer.timeout.connect(self.updateUI)

    def updateUI(self):
        self.ui.label_duration.setText(str(timedelta(0, self.net_graph.x_values[-1])))
        self.ui.label_total_emission.setText(str("{:.4e}".format(self.net_graph.y_values[-1] + self.hardware_graph.y_values[-1])))
        self.ui.label_car_km.setText(str("{:.4e}".format(float(self.ui.label_total_emission.text()) / 0.2)))
        self.ui.label_train_km.setText(str("{:.4e}".format(float(self.ui.label_total_emission.text()) / 0.002)))
        self.ui.label_plane_km.setText(str("{:.4e}".format(float(self.ui.label_total_emission.text()) / 0.1)))

    def start(self):
        self.timer.start()
        self.ui.startButton.setEnabled(False)
        self.ui.stopButton.setEnabled(True)
        self.ui.label_total_emission.setText("0")

    def stop(self):
        self.timer.stop()
        self.net_graph.x_values = [0 for _ in range(86400)]
        self.net_graph.y_values = [0 for _ in range(86400)]
        self.hardware_graph.x_values = [0 for _ in range(86400)]
        self.hardware_graph.y_values = [0 for _ in range(86400)]
        self.ui.startButton.setEnabled(True)
        self.ui.stopButton.setEnabled(False)
    

if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

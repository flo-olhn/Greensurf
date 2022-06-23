# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1194, 691)
        MainWindow.setStyleSheet(u"* {\n"
                                "color: #FFFFFF;\n"
                                "background-color: #101217;\n"
                                "font-size: 16px;\n"
                                "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_total_emission = QLabel(self.centralwidget)
        self.label_total_emission.setObjectName(u"label_total_emission")

        self.gridLayout_3.addWidget(self.label_total_emission, 3, 2, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_duration = QLabel(self.centralwidget)
        self.label_duration.setObjectName(u"label_duration")

        self.gridLayout_3.addWidget(self.label_duration, 2, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_4, 1, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.hardwareGraph = PlotWidget(self.centralwidget)
        self.hardwareGraph.setObjectName(u"hardwareGraph")

        self.gridLayout.addWidget(self.hardwareGraph, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setStyleSheet(u"*, QPushButton {\n"
"background-color: rgb(94, 255, 125);\n"
"border: none;\n"
"border-radius: 6px;\n"
"width: 100px;\n"
"height: 28px;\n"
"}\n"
"\n"
"*, QPushButton:hover {\n"
"background-color: #53E06F;\n"
"} ")

        self.horizontalLayout.addWidget(self.startButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setStyleSheet(u"QPushButton {\n"
"background-color: #FC002F;\n"
"border: none;\n"
"border-radius: 6px;\n"
"width: 100px;\n"
"height: 28px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #D40027;\n"
"}")

        self.horizontalLayout.addWidget(self.stopButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.networkGraph = PlotWidget(self.centralwidget)
        self.networkGraph.setObjectName(u"networkGraph")

        self.gridLayout.addWidget(self.networkGraph, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout, 1, 0, 3, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(16)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_plane_km = QLabel(self.centralwidget)
        self.label_plane_km.setObjectName(u"label_plane_km")
        self.label_plane_km.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_plane_km, 1, 2, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u"C:/Users/ouilh/OneDrive/Documents/Projet_E3/Greensurf/UI/assets/tgv.png"))
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setPixmap(QPixmap(u"C:/Users/ouilh/OneDrive/Documents/Projet_E3/Greensurf/UI/assets/avion.png"))
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u"C:/Users/ouilh/OneDrive/Documents/Projet_E3/Greensurf/UI/assets/auto.png"))
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.label_train_km = QLabel(self.centralwidget)
        self.label_train_km.setObjectName(u"label_train_km")
        self.label_train_km.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_train_km, 1, 1, 1, 1)

        self.label_car_km = QLabel(self.centralwidget)
        self.label_car_km.setObjectName(u"label_car_km")
        self.label_car_km.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_car_km, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_2, 3, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1194, 28))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Greensurf", None))
        self.label_total_emission.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Total (kg CO2e):", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Duration:", None))
        self.label_duration.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Network traffic emission (kg CO2eq)", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Hardware emission (kg CO2eq)", None))
        self.label_plane_km.setText(QCoreApplication.translate("MainWindow", u"0 km", None))
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_5.setText("")
        self.label_train_km.setText(QCoreApplication.translate("MainWindow", u"0 km", None))
        self.label_car_km.setText(QCoreApplication.translate("MainWindow", u"0 km", None))
    # retranslateUi


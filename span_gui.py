# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'span_gui.ui'
#
# Created: Tue Mar 27 18:15:56 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(829, 514)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.time_plot = PlotWidget(self.centralwidget)
        self.time_plot.setGeometry(QtCore.QRect(100, 50, 600, 180))
        self.time_plot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.time_plot.setObjectName(_fromUtf8("time_plot"))
        self.fft_plot = PlotWidget(self.centralwidget)
        self.fft_plot.setGeometry(QtCore.QRect(100, 270, 600, 180))
        self.fft_plot.setObjectName(_fromUtf8("fft_plot"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(560, 10, 111, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.buttonStart = QtGui.QPushButton(self.centralwidget)
        self.buttonStart.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.buttonStart.setObjectName(_fromUtf8("buttonStart"))
        self.buttonStop = QtGui.QPushButton(self.centralwidget)
        self.buttonStop.setGeometry(QtCore.QRect(190, 10, 75, 23))
        self.buttonStop.setObjectName(_fromUtf8("buttonStop"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Spectrum Analyser Ver. 1.0", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Choose Filter", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Highpass Filter", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Lowpass Filter", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "Bandpass Filter", None))
        self.buttonStart.setText(_translate("MainWindow", "Start", None))
        self.buttonStop.setText(_translate("MainWindow", "Stop", None))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


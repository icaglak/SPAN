# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'span_gui.ui'
#
# Created: Fri Apr 20 23:48:50 2018
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
        self.time_plot.setGeometry(QtCore.QRect(10, 50, 600, 180))
        self.time_plot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.time_plot.setObjectName(_fromUtf8("time_plot"))
        self.fft_plot = PlotWidget(self.centralwidget)
        self.fft_plot.setGeometry(QtCore.QRect(10, 240, 600, 180))
        self.fft_plot.setObjectName(_fromUtf8("fft_plot"))
        self.buttonStart = QtGui.QPushButton(self.centralwidget)
        self.buttonStart.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.buttonStart.setObjectName(_fromUtf8("buttonStart"))
        self.buttonStop = QtGui.QPushButton(self.centralwidget)
        self.buttonStop.setGeometry(QtCore.QRect(190, 10, 75, 23))
        self.buttonStop.setObjectName(_fromUtf8("buttonStop"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(630, 50, 191, 161))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.comboFilterType = QtGui.QComboBox(self.groupBox)
        self.comboFilterType.setGeometry(QtCore.QRect(80, 20, 101, 21))
        self.comboFilterType.setMaximumSize(QtCore.QSize(101, 16777215))
        self.comboFilterType.setAccessibleName(_fromUtf8(""))
        self.comboFilterType.setAccessibleDescription(_fromUtf8(""))
        self.comboFilterType.setEditable(False)
        self.comboFilterType.setObjectName(_fromUtf8("comboFilterType"))
        self.comboFilterType.addItem(_fromUtf8(""))
        self.comboFilterType.addItem(_fromUtf8(""))
        self.comboFilterType.addItem(_fromUtf8(""))
        self.comboFilterType.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineFilterCutoff = QtGui.QLineEdit(self.groupBox)
        self.lineFilterCutoff.setGeometry(QtCore.QRect(80, 70, 81, 20))
        self.lineFilterCutoff.setText(_fromUtf8(""))
        self.lineFilterCutoff.setMaxLength(5)
        self.lineFilterCutoff.setObjectName(_fromUtf8("lineFilterCutoff"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineFilterCutoff_2 = QtGui.QLineEdit(self.groupBox)
        self.lineFilterCutoff_2.setEnabled(False)
        self.lineFilterCutoff_2.setGeometry(QtCore.QRect(80, 100, 81, 20))
        self.lineFilterCutoff_2.setText(_fromUtf8(""))
        self.lineFilterCutoff_2.setMaxLength(5)
        self.lineFilterCutoff_2.setObjectName(_fromUtf8("lineFilterCutoff_2"))
        self.buttonApply = QtGui.QPushButton(self.groupBox)
        self.buttonApply.setGeometry(QtCore.QRect(60, 130, 75, 23))
        self.buttonApply.setObjectName(_fromUtf8("buttonApply"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboFilterType.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Spectrum Analyser Ver. 1.0", None))
        self.buttonStart.setText(_translate("MainWindow", "Start", None))
        self.buttonStop.setText(_translate("MainWindow", "Stop", None))
        self.groupBox.setTitle(_translate("MainWindow", "Filtering", None))
        self.comboFilterType.setItemText(0, _translate("MainWindow", "Raw Data", None))
        self.comboFilterType.setItemText(1, _translate("MainWindow", "Lowpass Filter", None))
        self.comboFilterType.setItemText(2, _translate("MainWindow", "Highpass Filter", None))
        self.comboFilterType.setItemText(3, _translate("MainWindow", "Bandpass Filter", None))
        self.label.setText(_translate("MainWindow", "Type: ", None))
        self.label_3.setText(_translate("MainWindow", "Cut-Off (Hz):", None))
        self.label_5.setText(_translate("MainWindow", "Cut-Off (Hz):", None))
        self.buttonApply.setText(_translate("MainWindow", "Apply", None))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


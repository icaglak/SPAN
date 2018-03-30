# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 16:30:48 2018

@author: Cagla
"""

import span_gui
import pyaudio
import sys
import numpy as np
import pyqtgraph as pg
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class SPAN(QMainWindow,span_gui.Ui_MainWindow):
     def __init__(self,parent=None):
        super(SPAN,self).__init__(parent)
        self.setupUi(self)
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024
        self.MAX_PLOT_SIZE = self.CHUNK * 50
        self.tdata = np.arange(self.MAX_PLOT_SIZE)/float(self.RATE)
        self.flabel = np.arange(self.CHUNK/2)*self.RATE/float(self.CHUNK)
        self.audioOBJ = pyaudio.PyAudio()
        
        self.stream = self.audioOBJ.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        self.total_data=[0 for i in range(self.MAX_PLOT_SIZE)]
        
        self.buttonStart.clicked.connect(self.startRec)
        self.buttonStop.clicked.connect(self.stopRec)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.guncelle)
        
        self.time_plot.setTitle("Audio Signal vs Time")       
        self.time_plot.setXRange(0, self.MAX_PLOT_SIZE/float(self.RATE))
        self.time_plot.showGrid(True,True)
        self.time_plot.addLegend()
        self.time_curve = self.time_plot.plot(pen=(24,215,248), name = "Time Domain Audio" )
        
        self.fft_plot.setTitle("Power vs Frequency Domain")
        self.fft_plot.showGrid(True,True)
        self.fft_plot.addLegend()
        self.fft_curve = self.fft_plot.plot(pen='y', name = "Power Spectrum")
        
     def guncelle(self):
         
         raw_data = self.stream.read(self.CHUNK)
         
         
         data_sample = np.fromstring(raw_data, dtype=np.int16)
         self.total_data = np.concatenate([self.total_data, data_sample ])          
         
         if len(self.total_data) > self.MAX_PLOT_SIZE:
           
           self.total_data = self.total_data[self.CHUNK:]
          
         self.time_curve.setData(self.tdata,self.total_data)
         
         fft_data = data_sample * np.hanning(len(data_sample))
         power_spectrum = 20 * np.log10(np.abs(np.fft.rfft(fft_data))/len(fft_data))
         
         self.fft_curve.setData(self.flabel,power_spectrum[:-1])
         self.fft_plot.enableAutoRange('xy', False)
    
    
     def startRec(self):
         self.timer.start(72)
     def stopRec(self):
         self.timer.stop()


app=QApplication(sys.argv)
form=SPAN()
form.show()
app.exec_()
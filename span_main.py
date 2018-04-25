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
from PyQt4 import QtCore, QtGui
from scipy.signal import*

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

        self.comboFilterType.currentIndexChanged.connect(self.filter_select)
        self.buttonApply.clicked.connect(self.generateTaps)
        self.b =[1.]
        self.filterOrder=201
          

     def guncelle(self):
         
         raw_data = self.stream.read(self.CHUNK)
         
         
         data_sample = np.fromstring(raw_data, dtype=np.int16)
         data_sample = lfilter(self.b,1,(data_sample.astype('float'))/32767.)
         self.total_data = np.concatenate([self.total_data, data_sample ])          
         
         if len(self.total_data) > self.MAX_PLOT_SIZE:
           
           self.total_data = self.total_data[self.CHUNK:]
          
         self.time_curve.setData(self.tdata,self.total_data)
         
         fft_data = data_sample * np.hanning(len(data_sample))
         power_spectrum = 20 * np.log10(np.abs(np.fft.rfft(fft_data))/len(fft_data))
         
         self.fft_curve.setData(self.flabel,power_spectrum[:-1])
         self.fft_plot.enableAutoRange('xy', False)

     def filter_select(self,index):
         
         if (index == 0):
             self.lineFilterCutoff.setEnabled(False)
             self.lineFilterCutoff_2.setEnabled(False)
             print 'Raw Data is Selected'
             
         elif (index == 1):
             self.lineFilterCutoff.setEnabled(True)
             self.lineFilterCutoff_2.setEnabled(False)   
             print 'Lowpass Filter is Selected with cutoff:',self.lineFilterCutoff.text()

         elif (index == 2):
             self.lineFilterCutoff.setEnabled(True)
             self.lineFilterCutoff_2.setEnabled(False)
             print 'Highpass Filter is Selected with cutoff:',self.lineFilterCutoff.text()

         else:
             self.lineFilterCutoff.setEnabled(True)
             self.lineFilterCutoff_2.setEnabled(True)
             print 'Bandpass Filter is Selected with cutoff:',self.lineFilterCutoff.text()
             
     def generateTaps(self):
         
         self.timer.stop()
         
         index = self.comboFilterType.currentIndex()
         f1 = int(self.lineFilterCutoff.text())
         f2 = int(self.lineFilterCutoff_2.text())
         if f1 > self.RATE/2:
             f1 = 1000
             self.lineFilterCutoff.setText(str(f1))
         if f2 > self.RATE/2:
             f2 = 5000
             self.lineFilterCutoff_2.setText(str(f2))
         if (index == 0):
             self.b = [1.]
         elif (index == 1): #LP
             self.b = firwin(self.filterOrder , 2*(float(f1)/self.RATE))
         elif (index == 2): #HP
             self.b = firwin(self.filterOrder, 2*(float(f1)/self.RATE) , pass_zero = False)
         else: #BP
             self.b = firwin(self.filterOrder, [2*(float(f1)/self.RATE),2*(float(f2)/self.RATE)] , pass_zero = False)
             
         self.timer.start(72)
        
     def startRec(self):
         self.timer.start(72)
     def stopRec(self):
         self.timer.stop()


app=QApplication(sys.argv)
form=SPAN()
form.show()
app.exec_()
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

class spmisc:
    def __init__(self):
        self.data = []

    def plotFreq(self, data):
        pts = 1024
        #amp = 10*np.log10(np.abs(np.fft.fft(data, pts)/(pts/2)))
        amp = 10*np.log10(np.abs(np.fft.fft(data, pts)/(2/2)))
        frq = fftfreq(pts, 0.01)
        xaxis = np.linspace(0,pts-1, pts)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.plot(xaxis, amp[0:pts], label='data', color='r', linewidth='2', linestyle='dashed')
        ax.set_xlabel('Frequency')
        ax.set_ylabel('Amplitude (dB)')
        plt.legend(loc='best')
        plt.show()
        pass

    def plot(self, data):
        #pts = len(data)
        pts = data.size
        print(pts)
        xaxis = np.linspace(0,pts-1, pts)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.plot(xaxis, data, label='data', color='r', linewidth='2', linestyle='solid')
        ax.set_xlabel('Time n')
        ax.set_ylabel('Amplitude')
        plt.legend(loc='best')
        plt.show()

    def plotMSE(self, data, names):
        ddim = data.ndim
        if ddim == 1:
            pts = data.size
        else:
            pts = data[1].size
        sdata = data.shape

        xaxis = np.linspace(0, pts-1, pts)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for i in range(len(data)):
            plt.plot(xaxis, 10*np.log10(data[i]), label=names[i], linewidth='2')
        ax.set_ylabel('Amplitude')
        plt.legend(loc='best')
        plt.show()

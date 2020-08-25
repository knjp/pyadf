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
        amp = 10*np.log10(np.abs(np.fft.fft(data, pts)/(pts/2)))
        frq = fftfreq(pts, 0.01)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.plot(frq, amp[0:pts], label='data', color='r', linewidth='2', linestyle='dashed')
        ax.set_xlabel('Frequency')
        ax.set_ylabel('Amplitude (dB)')
        plt.legend(loc='best')
        plt.show()
        pass


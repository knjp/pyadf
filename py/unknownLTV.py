import spconv
import numpy as np
import scipy as sp
from scipy import signal
import adfunknown

class unknown(adfunknown.adfunknown):
    def __init__(self, order):
        self._order = order
        taps = order
        edge = [0, 0.25, 0.3, 0.5]
        gain = [1.0, 0.00]
        #weight = [0.2, 1.0]
        self._unknown = sp.signal.remez(taps, edge, gain)
        #self._unknown = np.random.randn(self._order)
        self._conv = spconv.spconv(self._order)
        self._conv.coef = self._unknown
        self._arcoef = 0.0
        self.oldx = 0.0
        self._snr = 30
        self._sigmanoise = 0.00
        self._sigmax = 1
        pass

    @property
    def arcoef(self):
        return self._arcoef

    @arcoef.setter
    def arcoef(self, value):
        if value >= 0 and value < 1:
            self._arcoef = value
        else:
            self._arcoef = 0

    @property
    def snr(self):
        return self._snr

    @snr.setter
    def snr(self, value):
        self._snr = value
    
    def initunknown(self):
        self._conv = spconv.spconv(self._order)
        self._conv.coef = self._unknown
        SNRlinear = 10 ** (self._snr/10)
        npower = self._sigmax ** 2/SNRlinear
        self._sigmanoise = np.sqrt(npower)

    def input(self):
        x = np.random.randn(1) + self.oldx * self._arcoef
        xi = self._sigmax * (x/np.sqrt(1+self._arcoef))
        self.oldx = x
        return xi

    def output(self, input):
        d = self._conv.conv(input) + self._sigmanoise * np.random.randn(1)
        return d
           
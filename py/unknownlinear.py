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
        self.arcoef = 0.85
        self.oldx = 0.0
        self.sigmanoise = 0.01
        self.sigmax = 1
        pass

    def input(self):
        x = np.random.randn(1) + self.oldx * self.arcoef
        xi = self.sigmax * (x/np.sqrt(1+self.arcoef))
        self.oldx = x
        return xi

    def initunknown(self):
        self._conv = spconv.spconv(self._order)
        self._conv.coef = self._unknown

    def output(self, input):
        d = self._conv.conv(input) + self.sigmanoise * np.random.randn(1)
        return d
            
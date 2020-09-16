import spconv
import numpy as np
import scipy as sp
from scipy import signal

class spunknown:
    def __init__(self, order):
        self._order = order
        taps = order
        edge = [0, 0.25, 0.3, 0.5]
        gain = [1.0, 0.00]
        #weight = [0.2, 1.0]
        self._unknown = sp.signal.remez(taps, edge, gain)
        #self._unknown = np.array([0.25, 0.5, 0.25])
        #self._unknown = np.random.randn(self._order)
        self._conv = spconv.spconv(self._order)
        self._conv.coef = self._unknown
        pass

    def input(self):
        return np.random.randn(1)

    def initunknown(self):
        self._conv = spconv.spconv(self._order)
        self._conv.coef = self._unknown

    def output(self, input):
        d = self._conv.conv(input) + 0.01 * np.random.randn(1)
        return d
            
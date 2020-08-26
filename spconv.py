import numpy as np

class spconv:
    def __init__(self, order):
        self._order = order
        self._coef = np.ones(order)
        self._coef[0] = 1    # Initialization of the filter coefficients
        self._inputv = np.zeros(order)

    def conv(self, input):
        self._inputv = np.roll(self._inputv, 1)
        self._inputv[0] = input
        y = np.dot(self._inputv, self._coef)
        #print(self._inputv)
        #print(self._coef)
        return y

    @property
    def coef(self):
        return self._coef

    @coef.setter
    def coef(self, value):
        self._coef = value
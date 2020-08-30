import numpy as np

class adfalgorithm:
    def __init__(self, order):
        self._order = order
        self._mu = 0.1
        self._wcoef = np.zeros(self._order)
        self._winput = np.zeros(self._order)

    def initalgorithm(self):
        self._wcoef = np.zeros(self._order)
        self._winput = np.zeros(self._order)

    def initbuffer(self, input):
        self._winput = np.roll(self._winput, 1)
        self._winput[0] = input
        pass

    def update(self, e):
        self._wcoef = self._wcoef + self._mu * e * self._winput
        pass

    def iteration(self, input, desire):
        self._winput = np.roll(self._winput, 1)
        self._winput[0] = input
        y = np.dot(self._wcoef, self._winput)
        e = desire - y
        self.update(e)
        return y
        pass
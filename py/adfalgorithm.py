from abc import ABCMeta, abstractmethod
import numpy as np

class ADFalgorithm(metaclass=ABCMeta):
    def __init__(self, order):
        self._order = order
        self._wcoef = np.zeros(self._order)
        self._winput = np.zeros(self._order)
        self._name = "Adaptive Algorithm"

    def initalgorithm(self):
        self._wcoef = np.zeros(self._order)
        self._winput = np.zeros(self._order)

    def initbuffer(self, input):
        self._winput = np.roll(self._winput, 1)
        self._winput[0] = input

    @abstractmethod
    def update(self, e):
        pass

    def iteration(self, input, desire):
        self._winput = np.roll(self._winput, 1)
        self._winput[0] = input
        y = np.dot(self._wcoef, self._winput)
        e = desire - y
        self.update(e)
        return y
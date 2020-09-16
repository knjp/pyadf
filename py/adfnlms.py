import adfalgorithm as algo
import numpy as np

class nlmsalgorithm(algo.adfalgorithm):
    def __init__(self, order):
        super().__init__(order)
        self._alpha = 1.0
        self._name = "NLMS algorithm"


    def update(self, e):
        norm = np.dot(self._winput,self._winput)
        self._wcoef = self._wcoef + (self._alpha/norm) * e * self._winput
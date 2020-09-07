import numpy as np
import adfalgorithm 

class lmsalgorithm(adfalgorithm.adfalgorithm):
    def __init__(self, order):
        super().__init__(order)
        self._mu = 0.01
        self._name = "LMS algorithm"


    def update(self, e):
        self._wcoef = self._wcoef + self._mu * e * self._winput

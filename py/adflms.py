import numpy as np
import adfalgorithm 

class lmsalgorithm(adfalgorithm.adfalgorithm):
    def __init__(self, order):
        super().__init__(order)
        self._mu = 0.01
        self._name = "LMS algorithm"

    @property
    def mu(self):
        return self._mu
    
    @mu.setter
    def mu(self, value):
        if value > 0:
            self._mu = value
        else:
            print('The step size must be positive!')
            self._mu = 0.01

    def update(self, e):
        self._wcoef = self._wcoef + self._mu * e * self._winput

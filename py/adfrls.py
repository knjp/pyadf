import numpy as np
import adfalgorithm 

class rlsalgorithm(adfalgorithm.adfalgorithm):
    def __init__(self, order):
        super().__init__(order)
        self._lambda = 0.95
        self._sigma = 0.000001
        self._p = 1/self._sigma * np.eye(order)
        self._kvec = np.zeros(order)
        self._name = "RLS algorithm"

    def initalgorithm(self):
        super().initalgorithm()
        self._p = 1/self._sigma * np.eye(self._order)
        self._kvec = np.zeros(self._order)

    def update(self, e):
        self._wcoef = self._wcoef
        lmd = 1 / self._lambda
        m1 = np.dot(self._winput, self._p)
        m2 = np.dot(m1, self._winput)
        k = lmd * np.dot(self._p, self._winput) /(1 + lmd * m2)
        self._wcoef = self._wcoef + k * e
        k2 = np.outer(k,self._winput)
        self._p = lmd * self._p - lmd * np.dot(k2, self._p)


import spconv
import spmisc
import numpy as np
#import adfalgorithm as algo
import adfnlms as algo

class adfsimulation:
    def __init__(self, order, num):
        self._order = order
        self._num = num
        self.conv = spconv.spconv(self._order)
        #self.conv.coef = [0.2, 0.2, 0.2, 0.2, 0.2]
        self.conv.coef = np.random.randn(self._order)
        self.adf = algo.nlmsalgorithm(self._order)

    def simulation(self):
        for n in range(100):
            input = np.random.randn(1)
            d = self.conv.conv(input)
            self.adf.initbuffer(input)
        #
        eall = np.zeros(1000)
        for n in range (1000):
            input = np.random.randn(1)
            d = self.conv.conv(input)
            y = self.adf.iteration(input, d)
            err = d-y
            eall[n] = err

        b = spmisc.spmisc()
        print(self.conv.coef)
        print(self.adf._wcoef)
        b.plot(eall)
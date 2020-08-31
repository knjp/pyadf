import spconv
import spmisc
import numpy as np
#import adfalgorithm as algo
import adflms as lms
import adfnlms as nlms

class adfsimulation:
    def __init__(self, order, num):
        self._order = order
        self._num = num
        self.conv = spconv.spconv(self._order)
        #self.conv.coef = [0.2, 0.2, 0.2, 0.2, 0.2]
        self.conv.coef = np.random.randn(self._order)
        self.adf1 = lms.lmsalgorithm(self._order)
        self.adf2 = nlms.nlmsalgorithm(self._order)

    def simulation(self):
        for n in range(100):
            input = np.random.randn(1)
            d = self.conv.conv(input)
            self.adf1.initbuffer(input)
            self.adf2.initbuffer(input)
        #
        eall = np.zeros((2, 1000))
        for n in range (1000):
            input = np.random.randn(1)
            d = self.conv.conv(input) + 0.01 * np.random.randn()
            y = self.adf1.iteration(input, d)
            err = d-y
            eall[0][n] = err
            y = self.adf2.iteration(input, d)
            err = d-y
            eall[1][n] = err

        b = spmisc.spmisc()
        print(self.conv.coef)
        print(self.adf1._wcoef)
        b.plotMSE(eall)
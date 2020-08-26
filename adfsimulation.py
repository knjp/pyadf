import spconv
import spmisc 
import numpy as np

class adfsimulation:
    def __init__(self, order, num):
        self._order = order
        self._num = num
        self.conv = spconv.spconv(self._order)
        #self.conv.coef = [0.2, 0.2, 0.2, 0.2, 0.2]
        self.conv.coef = np.random.randn(5)
        self.wcoef = np.zeros(self._order)
        self.winput = np.zeros(self._order)

    def simulation(self):
        for n in range(10):
            input = np.random.randn(1)
            d = self.conv.conv(input)
            self.winput = np.roll(self.winput,1)
        #
        eall = np.zeros(100)
        for n in range (100):
            input = np.random.randn(1)
            d = self.conv.conv(input)
            self.winput = np.roll(self.winput,1)
            self.winput[0] = input
            y = np.dot(self.wcoef, self.winput)
            err = d-y
            eall[n] = err
            self.wcoef = self.wcoef + 0.1*err *self.winput

        b = spmisc.spmisc()
        print(self.conv.coef)
        print(self.wcoef)
        b.plot(eall)
import spconv
import spmisc
import numpy as np

class adfsimulation:
    def __init__(self, order, nlen, algos):
        self._order = order
        self._nlen = nlen
        self.conv = spconv.spconv(self._order)
        self.conv.coef = np.random.randn(self._order)
        self._algos = algos
        self._algonum = len(self._algos)
        self._nensemble = 50

    def ensemble(self):
        for na in range(self._algonum):
            self._algos[na].initalgorithm
        for n in range(2*self._order):
            input = np.random.randn(1)
            #d = self.conv.conv(input)
            for na in range(self._algonum):
                y = self._algos[na].initbuffer(input)

        eall = np.zeros((self._algonum, self._nlen))
        for n in range (self._nlen):
            input = np.random.randn(1)
            d = self.conv.conv(input) + 0.1 * np.random.randn()
            for na in range(self._algonum):
                y = self._algos[na].iteration(input, d)
                err = d-y
                eall[na][n] = err*err
        return eall

    def simulation(self):
        eall = np.zeros((self._algonum, self._nlen))
        for i in range(self._nensemble):
            print('Iteration No. ', i)
            es = self.ensemble()
            eall = eall + es

        eall = eall/self._nensemble
        b = spmisc.spmisc()
        b.plotMSE(eall)

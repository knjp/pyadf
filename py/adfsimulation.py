import spconv
import spmisc
import spunknown
import numpy as np

class adfsimulation:
    def __init__(self, order, nlen, algos, ensemble = 50):
        self._order = order
        self._nlen = nlen
        #self.conv = spconv.spconv(self._order)
        #self.conv.coef = np.random.randn(self._order)
        self._algos = algos
        self._algonum = len(self._algos)
        self._nensemble = ensemble
        self._unknown = spunknown.spunknown(self._order)

    def epoch(self):
        self._unknown.initunknown()
        for na in range(self._algonum):
            self._algos[na].initalgorithm()

        for n in range(2*self._order):
            input = self._unknown.input()
            d = self._unknown.output(input)
            for na in range(self._algonum):
                y = self._algos[na].initbuffer(input)

        errs = np.zeros((self._algonum, self._nlen))
        for n in range (self._nlen):
            input = self._unknown.input()
            d = self._unknown.output(input)
            for na in range(self._algonum):
                y = self._algos[na].iteration(input, d)
                e = d-y
                errs[na][n] = e*e
        return errs

    def simulation(self):
        eall = np.zeros((self._algonum, self._nlen))
        for i in range(self._nensemble):
            print('Iteration No. ', i)
            es = self.epoch()
            eall =  eall + es
        
        names =  []
        for i in range(self._algonum):
            names.append(self._algos[i]._name)

        eall2 = eall/(self._nensemble)
        print(eall2.shape)
        return eall2
        #b = spmisc.spmisc()
        #b.plotMSE(eall, names)

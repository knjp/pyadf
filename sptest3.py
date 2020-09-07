import adfsimulation
import adflms
import adfnlms

order = 31
nlen = 1000
lms = adflms.lmsalgorithm(order)
lms2 = adflms.lmsalgorithm(order)
lms2._mu = 0.005
nlms = adfnlms.nlmsalgorithm(order)

algos = [lms, nlms, lms2]
s = adfsimulation.adfsimulation(order, nlen, algos)
s.simulation()
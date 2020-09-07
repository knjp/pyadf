import adfsimulation
import adflms
import adfnlms

order = 131
nlen = 5000
ensemble = 100
lms = adflms.lmsalgorithm(order)
lms2 = adflms.lmsalgorithm(order)
lms2._mu = 0.005
lms2._name = "LMS (0.005)"
nlms = adfnlms.nlmsalgorithm(order)

algos = [lms, nlms, lms2]
s = adfsimulation.adfsimulation(order, nlen, algos, ensemble)
s.simulation()
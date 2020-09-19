from sys import argv
import adfsimulation as asim
import adflms
import adfnlms
import adfrls
import spmisc
import unknownlinear

if len(argv) == 2:
    arg = argv[1]
else:
    arg = 2

order = 31
nlen = 1500
ensemble = int(arg)
lms = adflms.lmsalgorithm(order)
lms._mu = 0.001
lms._name = "LMS (0.001)"
lms2 = adflms.lmsalgorithm(order)
lms2._mu = 0.005
lms2._name = "LMS (0.005)"
nlms = adfnlms.nlmsalgorithm(order)
rls = adfrls.rlsalgorithm(order)

#algos = [lms, nlms, lms2]
algos = [nlms, lms, lms2, rls]
unknown = unknownlinear.unknown(order)
s = asim.adfsimulation(order, nlen, algos, unknown, ensemble)
eall = s.simulation()

names =  []
for i in range(len(algos)):
    names.append(algos[i]._name)

b = spmisc.spmisc()
b.plotMSE(eall, names)

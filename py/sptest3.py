from sys import argv
import adfsimulation
import adflms
import adfnlms
import adfrls
import spmisc

if len(argv) == 2:
    arg = argv[1]
else:
    arg = 2

order = 131
nlen = 2000
ensemble = int(arg)
lms = adflms.lmsalgorithm(order)
lms2 = adflms.lmsalgorithm(order)
lms2._mu = 0.005
lms2._name = "LMS (0.005)"
nlms = adfnlms.nlmsalgorithm(order)
rls = adfrls.rlsalgorithm(order)

algos = [lms, nlms, rls]
s = adfsimulation.adfsimulation(order, nlen, algos, ensemble)
eall = s.simulation()

names =  []
for i in range(len(algos)):
    names.append(algos[i]._name)

b = spmisc.spmisc()
b.plotMSE(eall, names)

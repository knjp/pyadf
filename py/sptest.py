import spmisc
import numpy as np

x = spmisc.spmisc()
d = np.ones(200)
#x.plotFreq(d)

num = 100
r1 = np.random.randn(num)
xaxis = np.linspace(0,num-1, num)
r2 = np.random.randn(num)
#print(r1)
r3 = np.roll(r1,1)
#print(r3)

x.plot(r2)
import spconv
import numpy as np

r = spconv.spconv(4)
y = r.conv(3)
print(y)
y = r.conv(2)
print(y)
y = r.conv(5)
print(y)

r.coef = [0.2, 0.2, 0.2, 0.2, 0.2]
wcoef = np.zeros(5)
winput = np.zeros(5)

for n in range(10):
    input = np.random.randn(1)
    d = r.conv(input)
    winput = np.roll(winput,1)


eall = np.zeros(100)
for n in range (100):
    input = np.random.randn(1)
    d = r.conv(input)
    winput = np.roll(winput,1)
    winput[0] = input
    y = np.dot(wcoef, winput)
    err = d-y
    eall[n] = err
    wcoef = wcoef + 0.1*err *winput
    print(err)


import spmisc
b = spmisc.spmisc()
print(wcoef)
b.plot(eall)
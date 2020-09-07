import numpy as np

a = [[0, 1, 2], [3, 4, 5]]
print(len(a))
b = np.array(a)
c = b.shape
print(b.shape)

print(c[0])
print(c[1])

d = np.array([1,2,3,4,5])
e = d.shape
print(e[0])
print(d.ndim)
print(b.ndim)
#print(e[1])

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

pts = 500
a = np.random.randn(pts)
b = np.random.randn(pts)
x = np.linspace(0,pts-1, pts)

#plt.plot(x, a)
#plt.plot(x, b)
#plt.show()

r = np.random.randn(5, 4)
print('r = ', r)
rs = r.shape

print('r[2][2] = ' , r[2][2])

for i in range(rs[0]):
    b1 = r[i]
    print('r1 = ', b1)
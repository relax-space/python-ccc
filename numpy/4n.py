import numpy as np
from numpy import newaxis

a = np.floor(10*np.random.random((3, 4)))
print(a)
print(a.ravel())
print(a.reshape(6, 2))
print(a.T)
print(a)
a.resize(2, 6)
print(a)
print(np.hsplit(a, 2))

b = np.floor(10*np.random.random((2, 2)))
c = np.floor(10*np.random.random((2, 2)))
print(b)
print(c)
print(np.vstack((c, b)))
print(np.hstack((c, b)))

d = np.array([2, 3])
print(d[:, newaxis])

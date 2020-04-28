import numpy as np
from numpy import pi

a = np.array([10, 20, 30, 40])
b = np.arange(4)
c = a - b
print(c)
print(np.add(a, b))
print(a[2])
print(b**2)
print(a < 35)
print(10*np.sin(a))
print(a.sum())
print(a.min())
print(a.max())

d = np.array([[1, 1], [0, 1]])
e = np.array([[2, 0], [3, 4]])
print(d * e)
print(d @ e)
print(d.dot(e))

f = np.random.random((2, 3))
print(f)

g1 = np.linspace(0, pi, 3)
g = np.exp(g1*1j)
print(g, g.dtype)

h = np.arange(12).reshape(3, 4)
print(h)
print(r'h.sum(axis=0)', h.sum(axis=0))
print(r'h.sum(axis=1)', h.sum(axis=1))
print(r'h.min(axis=0)', h.min(axis=0))
print(r'h.min(axis=1)', h.min(axis=1))
print(r'h.cumsum(axis=0)', h.cumsum(axis=0))
print(r'h.cumsum(axis=1)', h.cumsum(axis=1))

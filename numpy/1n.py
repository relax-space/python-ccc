import numpy as np
from numpy import pi

a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))

b = np.array([6.0, 7, 8])
print(b)
print(type(b))
print(b.dtype)

c = np.array([(1, 2), (3, 4)], dtype=complex)
print(c)

print(np.zeros((3, 5)))
z = np.ones((2, 3, 4))
print(z)
print(z.dtype)
print(np.empty((3, 5)))

d = np.arange(10, 30, 5)
print(d)

e = np.linspace(0, 2, 9)
print(e)

f = np.linspace(0, 2*pi, 3)
print(f)

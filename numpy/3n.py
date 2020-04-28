import numpy as np

a = np.arange(10)**3
print(a)
a[:6:2] = -1000
print(a)
print(a[::-1])


def f(x, y):
    return 10*x + y


b = np.fromfunction(f, (5, 4), dtype=int)
print(b)
print(b[2, 3])
print(b[0:5, 1])
print(b[:, 1])
print(b[1:3, :])

c = np.array([[
    [0, 1, 2],
    [10, 12, 13]
],
    [
    [100, 101, 102],
    [110, 112, 113]
]])
print(c.shape)
print(c[1, ...])
print(c[..., 2])

for element in c.flat:
    print(element)

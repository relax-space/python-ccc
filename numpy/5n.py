import numpy as np

a = np.arange(12)
b = a
print(b is a)
b.shape = 3, 4
print(a.shape)


def f(x):
    print(id(x))


print(id(a))
f(a)

# 视图或浅拷贝
c = a.view()
print(c is a)
print(c.base is a)
c.shape = 2, 6
print(a.shape)
c[0, 4] = 1234
print(a)

# 切片数组会返回一个视图
s = a[:, 1:3]
s[:] = 10
print(a)

# 深拷贝
d = a.copy()
print(d is a)
print(d.base is a)
d[0, 0] = 99
print(a)

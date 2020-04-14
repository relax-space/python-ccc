# 列表内的项目不必全是相同的类型
a = ['jam', 10, True]
print(a)
print(a[0])
print(a[:2])
print(a[-2:])
print(a + ['mary', 100])
print(['hi']*3)

# 列表可以改变其中的元素
cubes = [1, 3, 5, 7, 9]
print(cubes, len(cubes))
cubes[0] = 0
print(cubes)
cubes.append(11)
print(cubes)
cubes.append(2**5)
print(cubes)
del cubes[0]
cubes[1:3] = [6, 10]
print(cubes)
cubes[1:3] = []
print(cubes)
cubes[:] = []
print(cubes)

# 也可以使用嵌套列表（在列表里创建其它列表）
x = ['jam', 'tom', 'lily']
y = [23, 30, 18]
z = [x, y]
print(z, len(z))
print(z[0][1])

# 所有的分切操作返回一个包含有所需元素的新列表
b = a[:]
print(id(b), id(a))

c = a
print(id(c), id(a))

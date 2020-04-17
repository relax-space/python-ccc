import math

s = 'hello,world\n'
# str() 函数返回一个用户易读的表达形式。 repr() 产生一个解释器易读的表达形式。
print(str(s))
print(repr(s))

# repr() 的参数可以是 Python 的任何对象
print(repr((2, 3, ('a', 'b'))))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=" ")
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# zfill(), 它会在数字的左边填充 0
print('-3.14'.zfill(8))
print('*abc1'.zfill(8))

# str.format() 的基本使用如下
print('we are {} friend, and say {}'.format('good', 'hi'))
print('{0} and {1}'.format('eggs', 'tomatos'))
print('{1} and {0}'.format('eggs', 'tomatos'))
print('hello {name}'.format(name='tom'))
print('{0} {name}'.format('hi', name='jack'))

# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化
print('PI\'s value is {}.'.format(math.pi))
print('PI\'s value is {!r}.'.format(math.pi))
print('PI\'s value is {:.3f}.'.format(math.pi))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for k, v in table.items():
    print('{:10}==>{:10d}'.format(k, v))
print('Jack:{0[Jack]:d},Dcab:{0[Dcab]:d},Sjoerd:{0[Sjoerd]:d}'.format(table)) # 必须都是0
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

print('PI\'s value is %s' % math.pi)
print('PI\'s value is %5.3f' % math.pi)

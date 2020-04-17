def hello():
    print("hello world~")


hello()


def area(width, heigh):
    return width * heigh


a = area(10, 20)
print(a)

# 函数变量作用域
a = 4


def test1():
    a = 10
    print("test1,a =", a)


def test2():
    print("test2,a =", a)


test1()
test2()
print("a =", a)

# keyword argument


def tree(name, heigh=100, year=6, color='red'):
    print(name, heigh, year, color)


tree('白杨')
tree(name='柳树', color='green')
tree('迎春花', heigh=50)

# 可变参数列表


def plus(*args):
    sum = 0
    for a in args:
        sum += a
    return sum


print(plus(1, 2, 3))
print(plus())
print(plus(1.1, 2, 5))

# 参数类型为List
list1 = [1, 2, 3, 4]


def change(list1):
    list1[0] = 100


change(list1)
print(list1)

# 匿名函数
sum = lambda arg1, arg2: arg1 + arg2
print(sum(1, 2))

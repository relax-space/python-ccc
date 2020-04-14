# 元组的元素不能修改
tup1 = ('Google', 'W3CSchool', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
print(tup1, tup2, tup3)
print(tup1 + tup2)
print(tup1[0])
print(tup1[2:4])

tup4 = ()
tup5 = (50,)  # 元组中只包含一个元素时，需要在元素后面添加逗号
print(type(tup4), type(tup5))

# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
del tup1
# print(tup1)  # name 'tup1' is not defined

# 元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组
print(('hi',)*3)
print(3 in tup2)
print(max(tup2))  # 5
print(min(tup2))  # 1

for x in tup3:
    print(x)

# 将列表转换为元组
list1 = ['jam', 'tom', 'jack']
tup1 = tuple(list1)
print(list1,tup1)

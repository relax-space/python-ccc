# list
a = [1, 2, 1, 2, 3, 1, 2, 3, 4]
print(a.count(1), a.count(2), a.count(3), a.count(4))
a.insert(2, 8)
print(a)
print(a.index(8))
a.remove(1)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.pop(2)
print(a)
b = a.copy()
a.clear()
print(b)
print(a)
a.extend(b)
print(a)
print(a.pop())

# list 列表推导式
vec = [1, 2, 3]
newvec = [x * 2 for x in vec]
newvec2 = [[x, x*2] for x in vec]
newvec3 = [x*2 for x in vec if x < 3]
newvec4 = [x*y for x in vec for y in vec]
newvec5 = [vec[i]*vec[i] for i in range(len(vec))]
print(newvec)
print(newvec2)
print(newvec3)
print("newvec4:", newvec4)
print("newvec5:", newvec5)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([f.strip() for f in freshfruit])

# list 嵌套列表解析
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
newmatrix = [[row[i] for row in matrix] for i in range(4)]
print(newmatrix)

# 集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)
print(a | b)
print(a ^ b)

c = {x for x in 'abcdef' if x not in 'abc'}
print(c)

# dict
student = {'name': 'mack', 'age': 20, 'favorate': 'basket', 'sex': True}
print(student['age'])
student['score'] = 370
print(student)
del student['favorate']
print(student)

list1 = list(student.values())
print(list1)
list2 = sorted(student.keys())
print(list2)

dict1 = dict([('jack', 1988), ('tom', 2001)])
print(dict1)
dict2 = {x: x**2 for x in (1, 2, 3, 4)}
print(dict2)
dict3 = dict(a=1, b=2, c=3)
print(dict3)

# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
for k, v in dict1.items():
    print(k, v)

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i, v in enumerate(['a', 'b', 'c', 'd']):
    print(i, v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合
questions = ['name', 'age', 'favorite color']
answers = ['jack', 20, 'blue']
for q, a in zip(questions, answers):
    print('What\'s your {0}? It is {1}.'.format(q, a))

# 要反向遍历一个序列，首先指定这个序列，然后调用 reversesd() 函数
for i in reversed(range(1, 10, 2)):
    print(i)

# sorted() 函数返回一个已排序的序列，并不修改原值
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# 键必须是唯一的,不可变的，如字符串，数字或元组;值可以取任何数据类型
dict1 = {'amy': 20, 'tom': 18, 'jack': 25, 'mimi': 20}
print(dict1, len(dict1))
print(dict1['amy'])
dict1['amy'] = 21
print(dict1)
del dict1['amy']
print(dict1)
dict1.clear()
print(dict1)
del dict1
# print(dict1) # name 'dict1' is not defined

dict2 = {'Name': 'W3CSchool', 'Age': 7, 'Name': '小菜鸟'}
print(dict2)

# 内置函数
dict3 = {'Name': 'W3CSchool', 'Age': 7, 'Class': 'First'}
print(len(dict3), type(dict3))
print(str(dict3))
dict4 = dict3.copy()
print(id(dict3), id(dict4))
dict5 = dict3.fromkeys([1, 2, 3, 4], 'ha')
print(dict5)
print(dict5.get(2))
print(dict5.get(0))
print(2 in dict5)
print(dict5.items())
print(dict5.keys())
print(dict5.values())
print(dict5.setdefault(5, 'hi'))
print(dict5)

dict6 = {6: 'he'}
dict5.update(dict6)
print(dict5)

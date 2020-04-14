import sys
# 迭代器有两个基本的方法：iter() 和 next()
list1 = [1, 2, 3, 4]
it = iter(list1)
print(next(it))
print(next(it))
for x in it:
    print(x, end=',')
print('\n')
list2 = ['a', 'b', 'c', 'd']
it2 = iter(list2)
while True:
    try:
        print(next(it2))
    except StopIteration:
        sys.exit()


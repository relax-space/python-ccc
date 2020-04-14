# while
total = 0
n = 100
i = 0
while i <= n:
    total += i
    i += 1
print("1~%d的总和为：%d" % (n, total))

# for
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)

edibles = ["ham", "spam", "eggs", "nuts"]
for food in edibles:
    if food == 'eggs':
        print('sorry, we hav\'t ', food)
        break
    print("you got dilicious ", food)
else:
    print("I am so glad: No eggs!")
print("Finally, I finished stuffing myself")

# range()函数。它会生成数列
for i in range(5):
    print(i)
for i in range(2, 4):
    print(i)
for i in range(0, 10, 4):
    print(i)
for i in range(-10, -100, -30):
    print(i)
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
print(list(range(5)))

# 循环语句可以有else子句;它在穷尽列表(以for循环)或条件变为假(以while循环)循环终止时被执行,但循环被break终止时不执行
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, "is a prime number.")

# pass语句什么都不做
for element in "Python":
    if element == "y":
        pass
    else:
        print(element)

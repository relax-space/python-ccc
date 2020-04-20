def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            return greater
        greater += 1


x = int(input("输入第一个数字："))
y = int(input("输入第二个数字："))

print("{}和{}的最小公倍数是：{}".format(x, y, lcm(x, y)))

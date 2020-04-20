def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(smaller, 0, -1):
        if((x % i == 0) and (y % i == 0)):
            return i


x = int(input("输入第一个数字："))
y = int(input("输入第二个数字："))

print("{}和{}的最大公约数是：{}".format(x, y, hcf(x, y)))

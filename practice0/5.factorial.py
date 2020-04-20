num = int(input("请输入要计算阶乘的数字："))
factorial = 1

if num < 0:
    print("很抱歉，负数没有阶乘。")
elif num == 0:
    print("{}的阶乘为1".format(num))
else:
    for i in range(2, num + 1):
        factorial *= i
    print("{}的阶乘为{}".format(num, factorial))

def is_armstrong(num):
    sum = 0
    n = len(str(num))

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10

    if num == sum:
        return True
    else:
        return False


lower = int(input("最小值："))
upper = int(input("最大值："))

for num in range(lower, upper + 1):
    isArmstrong = is_armstrong(num)
    if isArmstrong:
        print(num, end=",")

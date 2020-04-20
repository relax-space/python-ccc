nterms = int(input("你需要几项："))

a, b = 0, 1
count = 0

if nterms <= 0:
    print("请输入一个正整数。")
else:
    while count < nterms:
        print(a, end=",")
        a, b = b, a+b
        count += 1
print()


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1)+recur_fibo(n-2))


for i in range(nterms):
    print(recur_fibo(i), end=',')

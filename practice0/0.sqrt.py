import cmath

num = input("请输入一个数字:")
num_sqrt = float(num) ** 0.5
print('{0:0.3f} 的平方根为 {1:0.3f}'.format(float(num), num_sqrt))

num1 = int(input("请输入一个数字："))
num_sqrt1 = cmath.sqrt(num1)
print('{0} 的平方根为：{1:0.3f} + {2:0.3f}j'.format(num1, num_sqrt1.real, num_sqrt1.imag))

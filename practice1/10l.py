'''
编写一个程序，以给定的数字作为a的值来计算a + aa + aaa + aaaa的值。
假设将以下输入提供给程序：
9
然后，输出应为：
11106

提示：
如果将输入数据提供给问题，则应假定它是控制台输入。
'''

a = input("请输入一个正整数数字：")
print(int(a) + int(a*2) + int(a*3) + int(a*4))

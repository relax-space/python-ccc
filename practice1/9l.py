'''
编写一个接受句子并计算字母和数字数量的程序。
假设将以下输入提供给程序：
hello world! 123
Then, the output should be:
字母10
数字3

提示：
如果将输入数据提供给问题，则应假定它是控制台输入。
'''

str1 = input("请输入字符串：")
list1 = list(str1)
letterCnt = 0
numCnt = 0
for item in list1:
    if item.isdigit():
        numCnt += 1
    elif item.isalpha():
        letterCnt += 1

print("字母 {}".format(letterCnt))
print("数字 {}".format(numCnt))

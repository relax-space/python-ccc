'''
编写一个接受行序列作为输入的程序，并在将句子中的所有字符都排序之后打印行。
假设将以下输入提供给程序：
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

提示：
如果将输入数据提供给问题，则应假定它是控制台输入。
'''

str1 = input("请输入以逗号分隔的字符串：")
list1 = str1.split(",")
list1.sort()
print(','.join(list1))
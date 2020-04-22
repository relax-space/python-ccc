'''
编写一个程序，该程序接受由空格分隔的单词序列作为输入，
并在删除所有重复的单词并将其按字母数字顺序排序后打印这些单词。
假设将以下输入提供给程序：
Hello world world Practice makes perfect
Then, the output should be:
HELLO MAKES PERFECT PRACTICE WORLD

提示：
如果将输入数据提供给问题，则应假定它是控制台输入。
我们使用set容器自动删除重复的数据，然后使用sorted（）对数据进行排序。
'''

str1 = input("请输入以逗号分隔的字符串：")
list1 = str1.split(" ")
set1 = set(list1)
list1 = list(set1)
list1.sort()
print(','.join([item.upper() for item in list1]))

'''
编写一个程序，该程序接受以逗号分隔的单词序列作为输入，
并在按字母顺序对单词进行排序后以逗号分隔的顺序打印这些单词。
假设将以下输入提供给程序：没有,你好,袋,世界
然后，输出应为：袋,没有,你好,世界

提示：
如果将输入数据提供给问题，则应假定它是控制台输入。
'''

str1 = input("请输入以逗号分隔的单词序列：")
list1 = str1.split(",")
list1.sort(reverse=True)
print(','.join(list1))

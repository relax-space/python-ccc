f = open('./base/abc.txt', 'r+', encoding='UTF-8')
#方法用于截断文件
#f.truncate(9)
# print(f.read(9))
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readlines())

# for line in f:
#     print(line, end='')

for i in range(7):
    line = next(f)
    print(i, line)

print(f.write("\n春眠不觉晓。"))

# 如果要写入一些不是字符串的东西, 那么将需要先进行转换
print(f.write('\n'+str(500)))
print(f.writelines(['a\n','b']))
# print(f.tell()) # telling position disabled by next() call

# 从起始位置即文件首行首字符开始移动 3 个字符
f.seek(3, 0)
print(f.read(5))
print(f.isatty())
print(f.fileno())

f.close()

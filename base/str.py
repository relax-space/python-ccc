# 字符串可以使用 + 运算符串连接在一起，或者用 * 运算符重复
word = 'Hello' + ' '+'world!'
print(word)
print('Hello'' ''world!')
print(word[0])
print(word[-1])
print(word[:3])
print(word[2:5])
print(word[3:100])
print(len(word))
print(word * 3)
print('Mary said:', word)

# 反斜杠(\)转义特殊字符.另外，反斜杠可以作为续行符，表示下一行是上一行的延续
s = 'I don\'t know'
print(s, type(s), len(s))
print('c:\some\name')
print(r'c:\some\name')

s = 'I want you know\n\
    you are my\n\
    super man.'
print(s)

# 字符串不能被改变。向一个索引位置赋值会导致错误
'''
word = 'Help'
word[0] = 'x'
word[1:] = 'abc'
'''

# 关键字end可以被用于防止输出新的一行，或者在输出的末尾添加不同的字符
a, b = 0, 1
while b < 1000:
    print(b)
    a, b = b, a+b

a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

a, b = 0, 1
while b < 1000:
    print(b, end='-')
    a, b = b, a+b

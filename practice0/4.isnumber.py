def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except(TypeError, ValueError):
        pass

    return False

print(is_number('f'))
print(is_number('0'))
print(is_number('33'))
print(is_number('2.5f'))

# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四')) # True
# 版权号
print(is_number('©'))  # False

print("======== isdigit()")
print('3'.isdigit())
print('3t'.isdigit())
print("======== isnumeric()")
print(u'3'.isnumeric())
print(u'3t'.isnumeric())
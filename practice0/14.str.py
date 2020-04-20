str1 = input("请输入字符串：")

print(r"判断所有字符都是数字或者字母", str1.isalnum())
print(r"判断所有字符都是字母", str1.isalpha())
print(r"判断所有字符都是数字", str1.isdigit())
print(r"判断所有字符都是小写", str1.islower())
print(r"判断所有字符都是大写", str1.isupper())
print(r"判断所有单词都是首字母大写，像标题", str1.istitle())
print(r"判断所有字符都是空白字符、\t、\n、\r", str1.isspace())

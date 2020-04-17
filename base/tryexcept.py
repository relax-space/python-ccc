'''
while True:
    try:
        num = int(input("please input a number:"))
    except ValueError:
        print("Oops! That was no valid number!")
    else:
        print("Your input result is {}".format(num))
        break
'''

'''
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
'''


class MyError(Exception):
    def __init__(self, v):
        self.value = v

    def __str__(self):
        return repr(self.value)


try:
    raise MyError('aiyouwai')
except MyError as err:
    print("My exception occurred. err={}".format(err))
finally:
    print("我太难了。")

with open('./base/abc.txt', 'r+', encoding='UTF-8') as f:
    for line in f:
        print(line, end='')

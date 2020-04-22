'''
问题4
定义一个至少具有两个方法的类：
getString：从控制台输入获取字符串
printString：以大写形式输出字符串。还请包括简单的测试功能来测试类方法。

提示：
使用__init__方法构造一些​​参数
'''


class MyFunc:
    def __init__(self):
        pass

    def getString(self):
        self.say = input("请输入字符串：")

    def printString(self):
        print(self.say.upper())


myFunc = MyFunc()
myFunc.getString()
myFunc.printString()

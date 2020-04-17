import sys
import p.m1.support
from p.m2 import buzy

print('命令行参数如下：')
for i in sys.argv:
    print(i)
print('Python路径如下：', sys.path)

print(p.m1.support.__name__)
p.m1.support.func_print('marry')

func_print = p.m1.support.func_print
func_print('jack')

print(dir(p.m1.support))

buzy.func_self()

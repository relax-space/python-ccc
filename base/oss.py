import os

print(os.access('./base/abc.txt', os.X_OK))

retval = os.getcwd()
print("当前工作目录为 {}".format(retval))
os.chdir(r"E:\pythonPath\python-ccc\base")
retval = os.getcwd()
print("修改后工作目录为 {}".format(retval))
params = {"server": "mpilgrim", "database": "master",
          "uid": "sa", "pwd": "secret"}
str1 = ";".join(["{}={}".format(k, v) for k, v in params.items()])
print(str1)

list1 = str1.split(";")
list2 = str1.split(";", 1)
print(list1)
print(list2)

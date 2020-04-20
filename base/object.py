class people:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("{0} 说：我 {1} 岁。".format(self.name, self.age))


class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print("{0} 说：我 {1} 岁了，我在读 {2} 年级。".format(
            self.name, self.age, self.grade))


class speaker:
    topic = ''
    name = ''

    def __init__(self, t, n):
        self.topic = t
        self.name = n

    def speak(self):
        print("我叫 {0}，我是一个演说家，我的演讲主题是：{1}".format(self.name, self.topic))


class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        speaker.__init__(self, t, n)
        student.__init__(self, n, a, w, g)


test = sample('tom', 20, 80, '一', '世界末日之说')
test.speak()


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector ({},{})'.format(self.a, self.b)

    def __add__(self, other):
        return Vector(self.a+other.a, self.b+other.b)

    def __sub__(self, other):
        return Vector(self.a-other.a, self.b-other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1)
print(v2)
print(v1+v2)
print(v1-v2)

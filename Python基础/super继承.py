class My():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def foo(self):
        print("父类的方法")


class Son(My):
    def __init__(self, info,  name, gender, school, age):
        super(Son, self).__init__(name, age)  # 重写父类init方法
        self.info = info
        self.school = school
        self.gender = gender

    def foo(self):
        print("子类的方法")


you = Son("个人信息", 'xiaoming', 19, 1, 'sizhong')

print(you.name)  # xiaoming
print(you.age)  # sizhong
print(you.info)  # 个人信息
print(you.gender)  # 19
print(you.school)  # 1
you.foo()  # 子类的方法

"""
super重写父类的init方法，Python3中super(Class, self).__init__()可以直接写成super().__init__
"""

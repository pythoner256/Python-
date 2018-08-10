class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class B(A):
    def __init__(self, name, age, gender, school, professor, about):  # 子类__init__方法可以初始化自己的属性,但是要有父类的属性
        # super().__init__(name=name, age=age)
        super().__init__(name, age)  # 这里继承必须要写上父类的属性
        self.gender = gender
        self.professor = professor
        self.about = about
        self.school = school


b = B('xiaohong', 18, 1, 'sizhong', 'wuli', 'suiyi')
print(b.name)
print(b.age)


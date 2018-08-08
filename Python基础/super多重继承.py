"""单继承"""


class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m


class B(A):
    def __init__(self):
        # super().__init__()
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)  # 调用父类的add方法
        self.n += 3


b = B()  # self is <__main__.B object at 0x014430D0> @B.add

b.add(2)  # self is <__main__.B object at 0x014430D0> @A.add

print(b.n)  # 8


"""多重继承"""


class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print('self is {0} @C.add'.format(self))
        super().add(m)
        self.n += 4


class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        print('self is {0} @D.add'.format(self))
        super().add(m)
        self.n += 5


d = D()

d.add(2)  # self is <__main__.D object at 0x10ce10e48> @D.add
          # self is <__main__.D object at 0x10ce10e48> @B.add
          # self is <__main__.D object at 0x10ce10e48> @C.add
          # self is <__main__.D object at 0x10ce10e48> @A.add

print(d.n)  # 19

"""
调用 super() 的时候，实际上是实例化了一个 super 类,super既不是关键字也不是函数等其他数据结构
"""
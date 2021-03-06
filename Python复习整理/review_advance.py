# Pyhton 高级编程  不定期更新

"""== 和 is 判断两个对象是否相等和是否指向同一个对象"""
a = [1, 2]
a = b
a == b  # True 二者元素相同
a is b  # True 二者指向同一个对象

a = [1, 2, 3]
b = [1, 2, 3]
a == b  # True 二者元素相同
a is b  # False 两个对象并不是指向同一个对象

# 需要注意的是，在Python整型中-6到257这个数值之间是相同的

"""深拷贝和浅拷贝"""
# 浅拷贝

a_list = [1, 2]
b_list = a_list  # b_list 对 a_list进行的是浅拷贝，将数值和引用拷贝过来了，并不是开辟一个新的内存空间
b_list  # [1, 2]
a_list.append(3)  # 对被拷贝对象进行操作，对其浅拷贝的对象也会跟着改变
a_list  # [1, 2, 3]
b_list  # [1, 2, 3]

# 深拷贝

import copy

c = [3, 4]
d = copy.deepcopy(c)  # 对c深拷贝，将元素和引用一起拷贝了；新开辟了一个内存空间
c.pop()  # c[3];  d[3, 4]  对被拷贝对象操作不会影响对其深拷贝对象

e = [1, 2]
f = [3, 4]
g = [e, f]
h = copy.deepcopy(g)
e.append(5)  # e[1, 2, 5]
f.pop()  # 各列表的结果：f[3]   g[[1, 2, 5], [3]]      h[[1, 2], [3, 4]]

# 深拷贝意味着对拷贝对象里引用的对象也是进行深拷贝

# copy模块

a = [1, 2]
b = [3, 4]
c = [a, b]
d = copy.copy(c)  # 只是作第一层的深拷贝,对c里面引用的a和b对象还是浅拷贝

# 如果拷贝对象是不可变类型

copy.deepcopy()  # 依然是深拷贝
copy.copy()  # 都是进行浅拷贝


"""闭包"""


def func(num):
    def inner():  # 在一个函数体内定义一个函数，并且这个函数引用了外部函数的变量，则这个内部函数体称为闭包
        print(num)
    return inner

# 闭包的应用  输出一条直线方程式


def line(a, c):
    def inner(x):
        y = a*x + c
        print(y)
    return inner


y1 = line(2, 5)  # 确定一条 y = 2x+5 的直线方程；每次传入两个参数就能确定一条直线方程
y2 = line(3, 4)  # 确定一条 y= 3x+4 的直线方程
y1(1)  # 7； 得到y值
y2(2)  # 10

# 如此减少了参数的传递;提高代码可复用性

"""装饰器  装饰器的功能相当于在函数的基础上增加新的功能而不改变函数的原有的代码"""

# 假设定义了一个函数，在调用的时候希望加上一个验证功能


def wrapped(func):
    def inner():
        if True:
            print("已验证")
        else:
            print("验证未通过")
            func()
    return inner


@wrapped  # 相当于 foo = wrapped(foo)  此语法是Python独有的语法糖
def foo():
    print("加个验证功能")

# 有参数的装饰器


def wrapped(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
    return inner


@wrapped
def count(a, b, c, d):
    print("a=%d, b=%d, c=%d, d=%d" % (a, b, c, d))


count(10, 20, 30, 40)

# 有返回值的装饰器


def wrapped(func):
    def inner(*args, **kwargs):
        info = func(*args, **kwargs)
        return info
    return inner


@wrapped
def f():
    return "返回值"


rec = f()
print(rec)

# 2个装饰器


def wrapped1(func):
    def inner():
        func()
        return "<b>" + func() + "</b>"
    return inner


def wrapped2(func):
    def inner():
        return "<span>" + func() + "</span>"
    return inner


@wrapped2
@wrapped1  # 装饰器必须要遇到函数的时候才装饰，所以这里是先装饰1，再装饰2
def f1():
    return "2个装饰器"


info = f1()
print(info)  # <span><b>2个装饰器</b></span>


"""生成器generator"""

# 生成器：现在有个需求，需要一个100万个元素的列表，但是又不需要一次性拿出所有的元素，首先这个列表占用内容空间非常大，二是浪费了资源
# 生成器可以解决这个问题，生成器保存某种算法，在需要的时候就生成，在Python中，这种一边循环一边计算的机制，称为生成器：generator。

a_list = (i for i in range(10))  # 创建生成器第一种方法就是将列表生成式的中括号变成圆括号

next(a_list)  # 0
next(a_list)  # 1  直到元素全部被取出，抛出异常StopIteration

# 创建生成器第二种方法，使用yield关键字


def fibonacci():  # 生成前5位数的斐波那契数列
    x, y = 0, 1
    i = 1
    while i <= 5:
        x, y = x, x + y
        print(y, end=",")
        i += 1

# 将print 改成yield


def fibonacci():  # 第二种方法创建生成器
    x, y = 0, 1
    i = 1
    while i <= 5:
        x, y = x, x + y
        yield y
        """ 
        加入yield 关键字这个函数就不在是一个函数了；
        代码执行到yield就停止，直到下一次调用next()方法，代码继续从yield停止的地方开始执行
        """
        i += 1


gen = fibonacci()  # 调用这个生成器
for i in gen:
    print(i)

'''可迭代对象和迭代器'''
# 通俗的说可以用for循环遍历的就是可迭代对象；判断一个对象是否是可迭代对象可以用isinstance()方法来判断

from collections import Iterable

isinstance([], Iterable)  # True 列表是可迭代对象；同理tuple, dict, set, str等都是可迭代对象

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器；
# 迭代器对象从集合的第一个元素开始访问，直到最后抛出 StopIteration 错误表示无法继续返回下一个值了。
# 迭代器只能往前不会后退

from collections import Iterator

isinstance([], Iterator)  # False  集合数据类型都不是迭代器对象
isinstance((i for i in range(10)), Iterator)  # True 生成器都是迭代器对象

# iter()函数 可以将一个可迭代对象转换成迭代器对象

isinstance(iter('abc'), Iterator)  # True
isinstance(iter([]), Iterator)  # True

"""
凡是可作用于 for 循环的对象都是 Iterable 类型；
凡是可作用于 next() 函数的对象都是 Iterator 类型
集合数据类型如 list 、 dict 、 str 等是 Iterable 但不是 Iterator ，不过可以通过 iter() 函数获得一个 Iterator 对象。
"""

"""递归：递归就是引用自身的的意思"""

#
def func(n):
    """计算阶乘"""
    result = n
    for i in range(1, n):
        result *= i
    if n == 1:
        return 1
    else:
        return n*func(n-1)


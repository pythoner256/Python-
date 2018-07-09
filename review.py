# Python 非常基础的知识点，以后会不定期更新

# Python 自省
type(obj)  # 查看对象类型
id(obj)  # 查看对象的物理地址
isinstance(obj, t)  # 判断对象是否是指定的类型


"""Python帮助"""
dir(obj)  # 查询对象拥有的属性和方法
help(obj.func)  # 获得对象方法的使用


"""Python变量"""

# 1.Python变量只能用数字、下划线和字母表示，开头不能以数字开头
# 2.不能有空格
# 3.不能以Python关键字命名
# 4.慎用小写字母i和大写字母O,很容易看成是1和数字0


# 字符串
"""可以用双引号和单引号表示字符串"""
s = "this is a string."
ss = 'this is also a string'

# 字符串的一系列操作
s.title()  # 每个首字母大写
s.capitalize()  # 首字母大写，其他都是小写
s.lower()  # 全部小写
s.upper()  # 全部大写
s.strip()  # 删除空白
s.endswith('g')  # 判断是以什么结尾
s.startswith('g')  # 判断是以什么开头
sr = s+ss  # +号进行字符串拼接

# 字符串格式化format

s = 'zhe shi {}{}{} geshihua'.format('zi', 'fu', 'chuan')  # zhe shi zi fu chuan geshihua


# 制表符和换行符
"""
\n  # 换行符
\t  # 空格
"""

# 数字
"""
1.整数：数字之间可进行加减乘除和幂运算，除余，地板除法（+ - * / % **）
"""

"""列表"""

# 1.列表是可变类型；
# 2.列表的增：append(),在列表的末尾增加；extend(),将一个列表合并到另外一个列表(在末尾)；
#             insert(index,object),指定索引位置和对象；
# 3.列表的删：remove(value),指定某个元素进行删除，如果有重复的值，从左边开始只删除一个；del list[index],指定列表索引删除；
#             pop(),从列表末尾开始删，也可给定参数，参数就是索引，给定索引进行删除
#             如 pop(0):删除列表的第一个元素
# 4.列表的改：list[index] = value,通过重新赋值的方式改
# 5.列表的查：in 和 not in
# 6.切片：list[:], list[::], list[::-1]
# 7.排序和逆序：sorted(),暂时性排序，sort(),永久性排序；reverse(),逆序
# 8.列表的长度：len(list)
# 9.遍历整个列表：for i in list:
#                     pass
# 10.遍历的同时返回索引值：enumerate()函数;
# 11.列表生成式：l = [i for i in range(0,10)],l = [i**2 for i in range(10)]
#     可加入判断： l = [i for i in range(10) if i%2==0]
#     引入random模块，

"""元组"""

# 1.元组是不可变类型；
# 2.同样和列表一样通过索引来访问元素；
# 3.列表转换成元组：l = [1,2,3,4],t = tuple(l);同样元组也可以转换成列表，通过list()
# 4.元组里的元素同样可以通过for循环来遍历出来


"""字典"""

# 1.字典是Python中唯一的映射类型
# 2.访问字典的值,d = {"name":xiaom,"age":18}, 通过指定字典的键 dic['name'];
# 3.字典的增：通过添加键来增，dic["info"] = "this is info";
#             update()函数来增加一个字典到另外一个字典,放在末尾
# 4.字典的删：del()函数，del dic["name"];
# 5.改：指定键来改值，dic["age"] = 19;
# 6.查：in 和 not in用于判断键是否存在字典中；
#     get()函数和直接通过索引的方式获取值，如果字典不存在要查的键，get()函数不会报错，而直接通过索引的方式查如果不存在那就会报错
# 7.clear()方法,清空字典
# 8.遍历字典的键和值:  for key, value in dic.items():
#                     print(key,value)
# 9.按照顺序遍历键：for name in sorted(dic.keys):
#                     print(name)
# 10.遍历值，用values()方法，for value in dic.values():
#                                 pass
# 去除值里的重复值用set()函数：for value in set(dic.values()):
#                                 pass


# input和赋值
"""
python2 中的input会把input中的语句当作代码执行；
而Python3中会当作字符串执行，如果实现和Python2一样的功能，可在前面加上eval()方法
"""

# 赋值
a = 10
b = 20
a, b = b, a  # a,b的值调换

"""函数"""

# 1.定义一个函数：def func_name():
#                     pass
# 2.函数调用：func_name()
# 3.形参和实参：调用函数时给函数传递的变量是实参，而函数接收的变量是形参
# 4.位置形参：def func(name,age):
#                 pass
#            func('xiao',18),实参'xiao',18分别关联到name 和 age两个形参
# 5.关键字实参：def func(name,age):
#                 pass
#             func(age=18,name='xiao)
# 6.默认值：def func(name,age=18):
#             pass
#
#         foo('xiao')
# 7.返回值：def func(number,age):
#             return age+number
#          print(n = func(10,20))
# 8.传递任意数量的实参*args和**kwargs：def func(a,b,*args,**kwargs):
#                                         pass
#                                     func(10,20,30,40,num=100,s=200)
# 实参的传递是10,20分别给a和b,30和40给了args,将来封装成一个元组，num和s变量给了kwargs并将其封装成一个字典
# 9.局部变量和全局变量：num = 100
#                     def func():
#                         num = 200
#                     print(num)
#                     func()  # 函数打印的结果是 200
# 当一个函数的变量名既存在去全局变量和局部变量的时候，函数执行的过程会先去函数体中寻找这个变量，
# 也就是局部变量，如果未找到就去找全局变量；如果要修改全局变量需要用到global方法；
# 注意：假设定义了两个函数，第一个函数修改了全局变量，如果第二个函数也用到了这个变量，那么将来在使用这个变量的时候，调用的是第一个函数修改之后的变量


"""模块:模块是以扩展名为.py的文件"""


# import module_name  导入模块名
# import module_name as another_module_name  使用 as 给模块起别名
# from module_name import *  导入模块中的所有函数

"""包"""
# 在一个文件夹中放入空的 __init__.py 文件，这个文件夹就称为包，
# __all__方法用来指定将来导入模块的时候可被导入的函数或者变量
if __name__ == "__main__":  # 这段代码的是表示将来如果调用这个模块的时候是不会执行里面的函数的，如果是自己执行这个程序，就会从if 语句开始执行
    pass

"""类"""
# 类的命名规范：采用驼峰法命名，实例对象和模块名用小写格式，并在单词之间用下划线隔开；两个类之间用两个空行来隔开；方法之间一个空行隔开


class Lei():  # 定义一个类
    def __init__(self, name, age):  # 初始化属性name,age
        self.name = name
        self.age = age

    def func(self):  # 实例方法
        pass


lei = Lei('name', 18)  # 实例化一个对象
lei.func()  # 调用方法

# 类属性 类方法


class Lei():
    num = 10

    def __init__(self):
        self.initialize = 100  # 设置一个默认属性

    @classmethod  # 类方法
    def lei_func(cls):
        cls.num += 1  # 访问类属性


lei = Lei()
print(lei.num)  # 实例对象访问类属性；类属性是共有的（实例对象和类对象共有）
print(Lei.num)
print(lei.initialize)  # 实例对象访问实例属性
print(Lei.initialize)  # 类对象不能访问实例属性； # AttributeError: type object 'Lei' has no attribute 'age'
lei.lei_func()  # 实例对象调用类方法
Lei.lei_func()  # 类对象调用类方法

# 私有属性


class Lei():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__s = 100

    def func(self):
        self.__s += 1  # 私有属性可以在实例方法中使用


lei = Lei('name', 18)
print(lei.__s)  # 私有属性不能通过实例对象或者类对象在类外直接访问  # AttributeError: 'Lei' object has no attribute '__s'
print(lei.func())  # 实例方法调用私有属性，通过调用实例方法来间接使用私有属性

"""
    为什么私有属性不能在类外访问，是因为在定义私有属性的时候，通过名字重整的方法将私有属性的名字改了，可以通过dir()方法来查看:
    ['_Lei__s', '__class__', '__delattr__', '__dict__', '__dir__'............]
"""

# 另外 关于几个变量命名规则

"""
    以单一下划线开头的变量名(_X)不会被from module import*等语句导入
    前后有两个下划线的变量名(__X__)是系统定义的变量名，对解释器有特殊意义
    以两个下划线开头但不以下划线结尾的变量名(__X)是类的本地(私有)变量
"""

# 静态方法 静态方法基本上和一个全局函数相同


class Lei():
    num = 100

    def __init__(self):
        pass

    @staticmethod  # 静态方法
    def s_func(n):
        print(Lei.num+n)  # 看访问类属性


lei = Lei()
print(lei.s_func(100))  # 可通过实例对象和类对象访问静态方法
print(Lei.s_func(100))


# 类的继承

class Car():
    def __init__(self, make, time):
        self.make = make
        self.time = time

    def func(self):
        pass


class ElectricCar(Car):  # 继承的时候在括号写上要继承类的名字;可以继承多个类
    def __init__(self, make, time, model, style):
        super().__init__(make, time)  # 调用父类的__init__方法，将父类和子类关联起来  Python2中super需指定两个参数一个是子类的名字，一个是self
        self.model = model
        self.style = style

    def func(self):  # 重写父类方法
        pass

"""
    需要注意的是在多继承中调用同名父类的方法的时候，调用顺序是按照继承的顺序来的
"""


class Lei():
    def func(self):
        print('1')


class Er():
    def func(self):
        print('2')


class Zi(Lei, Er):
    pass


z = Zi()
z.func()  # 将来调用顺序是按照先去Lei调用,如果没有再去Er类里调用；相反，如果继承的时候括号里Er在前，那么就先去Er类里调用

"""导入类"""

# 1.导入单个类 from module_name import class_name
# 2.导入多个类 from module_name import class1_name, class2_name  中间用逗号隔开
# 3.导入整个模块 import module_name, 需要用到某个类的时候直接用module_name.class_name语法来访问类
# 4.导入模块里所有的类 from module_name import * 不推荐使用此方法，可能存在程序中与类同名的情况
# 5.导入模块的编码规范：先导入标准库，之后隔一行，再导入自己编写的模块


"""文件操作"""
# 读取

filename = 'test.txt'
with open(filename) as file_object:
    contents = file_object.read()  # 读取整个文件
    contents_rl = file_object.readline()  # 读取文件的第一行
    contents_rls = file_object.readlines()  # 逐行读取并显示在一行中;会有换行符，用strip()方法去除
    print(contents)

# 写入文件

with open('test.txt', 'w') as file_object:  # 如果文件不存在，函数open()会自动创建一个；w 写入模式；r 读取模式；a 附加模式
    file_object.write('whatever.\n')  # 写入多行的时候换行
    file_object.write('whatever you .\n')  # 写入多行的时候换行

# 需要注意是使用w写入模式的时候，会把之前文件的内容覆盖掉；如果需要附加到原先的内容则使用a附加模式

"""异常"""

# 使用try-except 代码块

"""
将可能出现异常的代码放在try里，当程序执行到try代码块，如果没问题则跳过except代码块，如果异常则执行except代码块
"""
try:
    print(5/0)
except ZeroDivisionError:
    print("分母不能为0")

# Exception
try:
    print(5/0)
except Exception as e:
    print(e)

# else  如果try代码块执行没问题就继续执行else代码块

try:
    print(5/0)
except Exception as e:
    print(e)
else:
    pass

"""存储数据 JSON库"""

# json.dump()  存储数据
import json

numbers = [1, 2, 3, 4, 5]
filename = 'number.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)  # 接收两个参数，第一个要存储的数据，用于存储数据的文件对象

# json.load()  读取数据

import json

filename = 'number.json'
with open(filename) as file_object:
    numbers = json.load(file_object)
    print(numbers)

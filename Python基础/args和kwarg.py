# -*- coding:utf-8 -*-


def foo(a, b, c=0, *args, **kwarg):
    print("a=%d, b=%d, c=%d, args=%s, kwarg=%s" % (a, b, c, args, kwarg))


A = (1, 2, 3)
B = {'key1': 1, "key2": 2}

foo(1, 2, 3, A)  # a=1, b=2, c=3, args=((1, 2, 3),), kwarg={}

foo(1, 2, 3, B)  # a=1, b=2, c=3, args=({'key1': 1, 'key2': 2},), kwarg={}

foo(1, 2, 3, A, B)  # a=1, b=2, c=3, args=((1, 2, 3), {'key1': 1, 'key2': 2}), kwarg={}

foo(1, 2, 3, n=10, m=100)  # a=1, b=2, c=3, args=(), kwarg={'n': 10, 'm': 100}

foo(1, 2, 3, *A)  # a=1, b=2, c=3, args=(1, 2, 3), kwarg={}

foo(1, 2, 3, **B)  # a=1, b=2, c=3, args=(), kwarg={'key1': 1, 'key2': 2}

foo(1, 2, 3, *A, **B)  # a=1, b=2, c=3, args=(1, 2, 3), kwarg={'key1': 1, 'key2': 2}

"""
在函数调用的时候传参，参数没有带*，按照位置参数的传给实参，打印结果args不会解包，而是当作一个整体打印出来；
如果参数带*，那么会在传递的时候解包成一个一个的元素，将来传递给args的时候会打包成一个元组输出；
kwarg的作用是将关键字参数打包成一个字典的形式输出
"""


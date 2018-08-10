# 计算阶乘
def func(n):
    result = n
    for i in range(1, n):
        result *= i
    if n == 1:
        return 1
    else:
        return n*func(n-1)


#print(func(10))


# 计算幂

def foo(x, n):
    result = 1
    for i in range(n):
        result = result*x
    if n == 0:
        return 1
    else:
        return x*foo(x, n-1)


y = foo(2, 3)
print(y)

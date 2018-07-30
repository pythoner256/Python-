def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield b
        a, b = b, a+b


if __name__ == "__main__":
    n = int(input("请输入一个数字："))
    fib_list = fib(n)
    alist = []
    for j in range(n):
        alist.append(next(fib_list))
    print(alist)
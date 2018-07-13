def bubble(n):
    for j in range(1, len(n)-1):
        for i in range(len(n)-j):
            if n[i] > n[i+1]:
                n[i], n[i+1] = n[i+1], n[i]
    print(n)


if __name__ == "__main__":
    n = eval(input("请输入一个数组: "))
    bubble(n)

def bubble(n):
    """从第一个元素开始依次和列表的元素进行比较，选出最大元素放到末尾"""
    for j in range(1, len(n)-1):
        for i in range(len(n)-j):
            if n[i] > n[i+1]:
                n[i], n[i+1] = n[i+1], n[i]
    print(n)


if __name__ == "__main__":
    n = eval(input("请输入一个数组: "))
    bubble(n)
"""
最优时间复杂度O(n)
最坏时间复杂度O(n平方)
"""

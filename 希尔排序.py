def func(alist):
    """
    希尔排序先将列表以一个步长隔断成几个序列，之后将各个序列还是按照插入排序进行排序；
    """
    n = len(alist)
    gap = n//2
    while gap > 0:  # 最外层循环控制gap
        for j in range(gap, n):  # 让第一个序列索引从gap步长开始和前面的元素进行判断
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap  # 下一个比较的元素之间索引距离是gap
                else:
                    break
        gap //= 2  # 每次让步长都取半


if __name__ == "__main__":
    alist = eval(input("请输入一个数组："))
    func(alist)
    print(alist)

"""
最优时间复杂度根据步长的设计不用结果都不同；
最坏时间复杂度O(n的平方)
"""

def insert_sort(alist):
    """
    插入排序 依然把列表看成无序和有序，和选择排序不用的是，插入排序操作的是有序序列，
    而选择排序是操作无序序列，元素拿过来是有固定位置的，插入排序元素拿过来需要和有序序列挨个比较
    """
    for j in range(1, len(alist)):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break


if __name__ == "__main__":
    alist = eval(input("请输入一个数组: "))
    insert_sort(alist)
    print(alist)

"""
最优时间复杂度，序列就是递增序列，时间复杂度O(n);
最坏时间复杂度，O(n平方)
"""


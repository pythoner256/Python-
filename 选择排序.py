def select_sort(n):
    """
    认为列表分成有序和无序两部分，每次排序都从无序的列表中筛选最小元素添加到有序列表中
    """
    for j in range(len(n)-1):
        min_index = j  # 记录最小值的下标
        for i in range(j+1, len(n)):
            if n[min_index] > n[i]:
                min_index = i  # 交换最小值下标
        n[j], n[min_index] = n[min_index], n[j]
    print(n)


if __name__ == "__main__":
    n = eval(input("请输入与一个数组："))
    select_sort(n)

# 最优时间复杂度O(n平方)
# 最坏时间复杂度O(n平方)

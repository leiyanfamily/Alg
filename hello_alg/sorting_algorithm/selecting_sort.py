"""
选择排序
原理：开启一个循环，每轮从未排序的区间中选择最小的元素，将其放到已排序区间的末尾
"""


def select_sort(arr):
    start_index = 0
    end_index = len(arr) - 1
    while start_index < end_index:
        min_index = start_index
        for i in range(start_index + 1, end_index + 1):
            if arr[i] < arr[min_index]:
                min_index = i
        arr[start_index], arr[min_index] = arr[min_index], arr[start_index]
        start_index += 1
    return arr


"""
选择排序：
外循环： 未排序区间[0, n-1]
内循环： 找到未排序区间最小值[i + 1, n]
算法复杂度： O(n的平方)
空间复杂度： O(1)
非稳定排序： 相等元素的位置可能会被改变
"""
def new_select_sort(arr):
    n = len(arr)
    # 外循环： 未排序区间为[i, n - 1]
    for i in range(n - 1):
        # 内循环 找到未排序区间内的最小元素
        k = i
        for j in range(i + 1, n):
            if arr[j] < arr[k]:
                k = j
        arr[k], arr[i] = arr[i], arr[k]
    return arr

if __name__ == '__main__':
    arr = [9, 4, 6, 3, 8, 2, 7]
    # print(select_sort(arr))
    print(new_select_sort(arr))

"""
冒泡排序
原理：通过连续的比较与交换相邻元素实现排序
"""

def bubble_sort(arr):
    start_index = 0
    for i in range(start_index, len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



def new_bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == '__main__':
    arr = [9, 4, 6, 3, 8, 2, 0, 0, 7]
    # bubble_sort(arr)
    new_bubble_sort(arr)
    print(arr)
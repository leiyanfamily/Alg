"""
归并排序

"""

def merge(nums, left, mid, right):
    tmp = [0] * (right - left + 1)
    i, j, k = left, mid + 1, 0
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
        k += 1
    while i <= mid:
        tmp[k] = nums[i]
        i += 1
        k += 1
    while j <= right:
        tmp[k] = nums[j]
        j += 1
        k += 1
    for k in range(0, len(tmp)):
        nums[left + k] = tmp[k]


def merge_sort(nums, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)
    merge(nums, left, mid, right)

if __name__ == '__main__':
    my_nums = [9, 3, 5, 2, 6, 7, 8]

    merge_sort(my_nums, 0, len(my_nums) - 1)
    print(my_nums)
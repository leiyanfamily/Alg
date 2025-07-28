def binary_search(arr, target):
    """二分查找"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    nums = [1, 2,5, 8,9, 10, 23, 34, 56, 57, 61, 65]
    print(binary_search(nums, 56))

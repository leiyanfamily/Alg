"""
快速排序（分治策略的排序算法）
时间复杂度： nlogn
"""

def partition(nums: list[int], left: int, right: int) -> int:
    """哨兵划分
    目的： 将比基准值大的交换到基准值的右侧，将比基准值小的交换到基准值的左侧，并将基准值交换到合适的位置
    """
    # 以 nums[left] 为基准数
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1  # 从右向左找首个小于基准数的元素
        while i < j and nums[i] <= nums[left]:
            i += 1  # 从左向右找首个大于基准数的元素
        # 元素交换
        nums[i], nums[j] = nums[j], nums[i]
    # 将基准数交换至两子数组的分界线
    nums[i], nums[left] = nums[left], nums[i]
    return i  # 返回基准数的索引

def quick_sort(nums: list[int],  left:int, right:int):
    if left >= right:
        return
    pivot = partition(nums, left, right)
    quick_sort(nums, left, pivot - 1)
    quick_sort(nums, pivot + 1, right)

if __name__ == '__main__':
    nums = [5, 4, 6, 3, 8, 2, 0, 0, 7]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)

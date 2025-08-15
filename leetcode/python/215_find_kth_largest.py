"""
215. 数组中的第K个最大元素
中等
相关标签
premium lock icon
相关企业
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_sort(nums, k)

    def quick_sort(self, nums, k):
        # 随机选择一个数作为枢纽
        pivot = random.choice(nums)
        # 将大于，等于，小于pivot的数分别放到不同的数组中
        g_list, e_list, l_list = [], [], []
        for num in nums:
            if num > pivot:
                g_list.append(num)
            elif num < pivot:
                l_list.append(num)
            else:
                e_list.append(num)
        # 根据三个子数组的长度与k的比较，决定递归方向
        # 如果k小于len(g_list), 说明所求值在g_list中
        if k <= len(g_list):
            return self.quick_sort(g_list, k)
        # 第k大的元素在l_list中，
        elif k > len(g_list) + len(e_list):
            # 调整k的传给你读，减去g_list和e_list的长度
            return self.quick_sort(l_list, k - (len(g_list) + len(e_list)))
        # 第k大的元素在equal数组中
        return pivot


if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    s = Solution()
    print(s.findKthLargest(nums, k))


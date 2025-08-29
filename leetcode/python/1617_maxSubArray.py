"""
面试题 16.17. 连续数列
简单
给定一个整数数组，找出总和最大的连续数列，并返回总和。

示例：

输入： [-2,1,-3,4,-1,2,1,-5,4]
输出： 6
解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶：

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

"""
import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min = 0
        result = -math.inf
        total = 0
        for i in nums:
            total += i
            result = max(result, total - min)
            if total < min:
                min = total
        return result


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    print(solution.maxSubArray(nums))
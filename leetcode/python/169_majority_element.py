"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""
from typing import List


class Solution(object):
    def majorityElement(self, nums):
        num_count = {}
        length = len(nums)
        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1
            if num_count[num] > length / 2:
                return num


class Solution1:

    def getMajority(self, nums: List[int], left, right):

        if left == right:
            return nums[left]

        # 递归划分左右区间
        mid = left + (right - left) // 2
        maxLeft = self.getMajority(nums, left, mid)
        maxRight = self.getMajority(nums, mid + 1, right)

        # 如果左边众数 = 右边的众数
        if maxLeft == maxRight:
            return maxLeft

        # 如果左右众数不相等
        else:
            leftCnt, rightCnt = 0, 0

            # 合并区间找众数
            for i in range(left, right + 1):
                if maxLeft == nums[i]:
                    leftCnt += 1

                if maxRight == nums[i]:
                    rightCnt += 1

            if leftCnt >= rightCnt:
                return maxLeft
            else:
                return maxRight

    def majorityElement(self, nums: List[int]) -> int:

        return self.getMajority(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    nums = [2,2,1,1,1,2,2]
    # solution = Solution()
    solution = Solution1()
    print(solution.majorityElement(nums))
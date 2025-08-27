"""
LCR 158. 库存管理 II
仓库管理员以数组 stock 形式记录商品库存表。stock[i] 表示商品 id，可能存在重复。请返回库存表中数量大于 stock.length / 2 的商品 id。

 

示例 1：

输入：stock = [6, 1, 3, 1, 1, 1]
输出：1
 

提示：

1 <= stock.length <= 50000
给定数组为非空数组，且存在结果数字

分治：
思路

如果数 a 是数组 nums 的众数，如果我们将 nums 分成两部分，那么 a 必定是至少一部分的众数。

我们可以使用反证法来证明这个结论。假设 a 既不是左半部分的众数，也不是右半部分的众数，
那么 a 出现的次数少于 l / 2 + r / 2 次，其中 l 和 r 分别是左半部分和右半部分的长度。
由于 l / 2 + r / 2 <= (l + r) / 2，
说明 a 也不是数组 nums 的众数，因此出现了矛盾。所以这个结论是正确的。

这样以来，我们就可以使用分治法解决这个问题：将数组分成左右两部分，分别求出左半部分的众数 a1 以及右半部分的众数 a2，随后在 a1 和 a2 中选出正确的众数。

算法

我们使用经典的分治算法递归求解，直到所有的子问题都是长度为 1 的数组。长度为 1 的子数组中唯一的数显然是众数，直接返回即可。
如果回溯后某区间的长度大于 1，我们必须将左右子区间的值合并。如果它们的众数相同，那么显然这一段区间的众数是它们相同的值。
否则，我们需要比较两个众数在整个区间内出现的次数来决定该区间的众数。


"""

from typing import List
import time
from collections import Counter

# class Solution:
    # def inventoryManagement(self, stock: List[int]) -> int:
    #     for i in stock:
    #         if stock.count(i) > len(stock) / 2:
    #             return i
    #     return -1

    # def inventoryManagement(self, stock: List[int]) -> int:
    #     stock_dict = {}
    #     for i in stock:
    #         if i not in stock_dict:
    #             stock_dict[i] = 1
    #             if stock_dict[i] > len(stock) / 2:
    #                 return i
    #             continue
    #         stock_dict[i] += 1
    #         if stock_dict[i] > len(stock) / 2:
    #             return i
    #     return -1

    # def inventoryManagement(self, stock: List[int]) -> int:
    #     counter = Counter(stock)
    #     for i in dict(counter):
    #         if counter[i] > len(stock) / 2:
    #             return i
    #     return -1

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def majority_element_rec(lo, hi) -> int:
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)
    

if __name__ == "__main__":
    stock = [1, 2, 1, 3, 1, 1]
    print(len(stock))
    sol = Solution()
    time1 = time.time()
    # print(sol.inventoryManagement(stock))
    print(sol.majorityElement(stock))
    time2 = time.time()
    print(time2 - time1)
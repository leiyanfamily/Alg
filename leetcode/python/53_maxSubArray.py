"""
53. 最大子数组和
中等
相关企业
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组是数组中的一个连续部分。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23
 

提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。

方法二：分治
思路和算法

这个分治方法类似于「线段树求解最长公共上升子序列问题」的 pushUp 操作。 也许读者还没有接触过线段树，没有关系，方法二的内容假设你没有任何线段树的基础。
当然，如果读者有兴趣的话，推荐阅读线段树区间合并法解决多次询问的「区间最长连续上升序列问题」和「区间最大子段和问题」，还是非常有趣的。

我们定义一个操作 get(a, l, r) 表示查询 a 序列 [l,r] 区间内的最大子段和，那么最终我们要求的答案就是 get(nums, 0, nums.size() - 1)。
如何分治实现这个操作呢？对于一个区间 [l,r]，我们取 m=⌊l+r⌋ / 2，对区间 [l,m] 和 [m+1,r] 分治求解。当递归逐层深入直到区间长度缩小为 1 的时候，递归「开始回升」。
这个时候我们考虑如何通过 [l,m] 区间的信息和 [m+1,r] 区间的信息合并成区间 [l,r] 的信息。最关键的两个问题是：

我们要维护区间的哪些信息呢？
我们如何合并这些信息呢？
对于一个区间 [l,r]，我们可以维护四个量：

lSum 表示 [l,r] 内以 l 为左端点的最大子段和
rSum 表示 [l,r] 内以 r 为右端点的最大子段和
mSum 表示 [l,r] 内的最大子段和
iSum 表示 [l,r] 的区间和
以下简称 [l,m] 为 [l,r] 的「左子区间」，[m+1,r] 为 [l,r] 的「右子区间」。
我们考虑如何维护这些量呢（如何通过左右子区间的信息合并得到 [l,r] 的信息）？对于长度为 1 的区间 [i,i]，四个量的值都和 nums[i] 相等。对于长度大于 1 的区间：

首先最好维护的是 iSum，区间 [l,r] 的 iSum 就等于「左子区间」的 iSum 加上「右子区间」的 iSum。
对于 [l,r] 的 lSum，存在两种可能，它要么等于「左子区间」的 lSum，要么等于「左子区间」的 iSum 加上「右子区间」的 lSum，二者取大。
对于 [l,r] 的 rSum，同理，它要么等于「右子区间」的 rSum，要么等于「右子区间」的 iSum 加上「左子区间」的 rSum，二者取大。
当计算好上面的三个量之后，就很好计算 [l,r] 的 mSum 了。我们可以考虑 [l,r] 的 mSum 对应的区间是否跨越 m——它可能不跨越 m，也就是说 [l,r] 的 mSum 可能是「左子区间」的 mSum 和 「右子区间」的 mSum 中的一个；它也可能跨越 m，可能是「左子区间」的 rSum 和 「右子区间」的 lSum 求和。三者取大。
这样问题就得到了解决。

"""

import math
from typing import List


class State:

    def __init__(self, l, r, m, i):
        self.l_sum = l  # 以左端点为起点的最大和
        self.r_sum = r  # 以右端点为起点的最大和
        self.m_sum = m  # 区间的最大和
        self.i_sum = i  # 区间和


class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     min = 0
    #     result = -math.inf
    #     total = 0
    #     for i in nums:
    #         total += i
    #         result = max(result, total - min)
    #         if min > total:
    #             min = total
    #     return result
    

    def maxSubArray(self, nums: List[int]) -> int:
        return self.get_info(nums, 0, len(nums) - 1).m_sum

    def get_info(self, nums: List, l: int, r: int) -> State:
        if l == r:
            return State(nums[l], nums[l], nums[l], nums[l])
        mid = (l + r) // 2
        l_state = self.get_info(nums, l, mid)
        r_state = self.get_info(nums, mid+1, r)
        return self.push_up(l_state, r_state)
    
    def push_up(self, l_state: State, r_state: State) -> State:
        l_sum = max(l_state.l_sum, l_state.i_sum + r_state.l_sum)
        r_sum = max(r_state.r_sum, r_state.i_sum + l_state.r_sum)
        m_sum = max(max(l_state.m_sum, r_state.m_sum), l_state.r_sum + r_state.l_sum)
        i_sum = l_state.i_sum + r_state.i_sum
        return State(l_sum, r_sum, m_sum, i_sum)



if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]

    solution = Solution()
    print(solution.maxSubArray(nums))
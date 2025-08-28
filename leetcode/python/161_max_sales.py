"""
LCR 161. 连续天数的最高销售额
简单

某公司每日销售额记于整数数组 sales，请返回所有 连续 一或多天销售额总和的最大值。

要求实现时间复杂度为 O(n) 的算法。

 a

示例 1：

输入：sales = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：[4,-1,2,1] 此连续四天的销售总额最高，为 6。
示例 2：

输入：sales = [5,4,-1,7,8]
输出：23
解释：[5,4,-1,7,8] 此连续五天的销售总额最高，为 23。 
 

提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
"""

from typing import List
import math


class Solution:
    def maxSales(self, sales: List[int]) -> int:
        min = 0
        res = -math.inf
        total = 0
        for i in sales:
            total += i
            res = max(res, total - min)
            if total < min:
                min = total
        return res
    
if __name__ == "__main__":
    sales = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
    sol = Solution()
    print(sol.maxSales(sales))
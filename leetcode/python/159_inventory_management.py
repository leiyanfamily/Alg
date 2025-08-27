"""
LCR 159. 库存管理 III
简单

仓库管理员以数组 stock 形式记录商品库存表，其中 stock[i] 表示对应商品库存余量。请返回库存余量最少的 cnt 个商品余量，返回 顺序不限。

 

示例 1：

输入：stock = [2,5,7,4], cnt = 1
输出：[2]
示例 2：

输入：stock = [0,2,3,6], cnt = 2
输出：[0,2] 或 [2,0]
 

提示：

0 <= cnt <= stock.length <= 10000

	0 <= stock[i] <= 10000
"""

from typing import List

class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        # return sorted(stock)[:cnt]
        return self.merge_sort(stock, 0, len(stock) - 1)[:cnt]
    

    def merge_sort(self, nums, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)
        return nums
    
    def merge(self, nums, left, mid, right):
        result = []
        i, j= left, mid + 1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                result.append(nums[i])
                i += 1
            else:
                result.append(nums[j])
                j += 1
        if i <= mid:
            result.extend(nums[i: mid + 1])
        if j <= right:
            result.extend(nums[j: right + 1])
        nums[left: right + 1] = result
        


if __name__ == '__main__':
    stock = [0,0,2,3,2,1,1,2,0,4]
    cnt = 10
    sol = Solution()
    print(sol.inventoryManagement(stock, cnt))
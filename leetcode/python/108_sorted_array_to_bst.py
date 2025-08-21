"""
将有序数组转换为二叉搜索树

给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。

输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 按 严格递增 顺序排列
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.dfs(nums, 0, len(nums)-1)

    def dfs(self, nums, start, end):
        if start > end:
            return
        mid = (start + end) // 2
        return TreeNode(nums[mid], self.dfs(nums, start, mid-1), self.dfs(nums, mid+1, end))

def befsort(node):
    if node is None:
        return
    befsort(node.left)
    print(node.val)
    befsort(node.right)


if __name__ == '__main__':
    nums = [-10,-3,0,5,9]
    s = Solution()
    node = s.sortedArrayToBST(nums)
    befsort(befsort(node))


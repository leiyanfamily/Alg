"""
106. 从中序与后序遍历序列构造二叉树
中等

给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。

 

示例 1:
      3
    /   \
  9      20
        /  \
      15    7

输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]
示例 2:

输入：inorder = [-1], postorder = [-1]
输出：[-1]
 

提示:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder 和 postorder 都由 不同 的值组成
postorder 中每一个值都在 inorder 中
inorder 保证是树的中序遍历
postorder 保证是树的后序遍历
"""
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.my_build_tree(inorder, postorder)

    def my_build_tree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        in:   [[左子树], root, [右子树]]
        post: [[左子树], [右子树], root]
        """
        if not inorder:
            return
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        root = postorder[-1]
        in_root_index = inorder.index(root)
        post_root_index = postorder.index(root)

        root_node = TreeNode(root)
        left_node = self.my_build_tree(inorder[:in_root_index], postorder[:in_root_index])
        right_node = self.my_build_tree(inorder[in_root_index+1:], postorder[in_root_index:post_root_index])
        root_node.left = left_node
        root_node.right = right_node
        return root_node



if __name__ == "__main__":
    # inorder = [9,3,15,20,7]
    # postorder = [9,15,7,20,3]
    inorder = [1, 2, 3, 4]
    postorder = [4, 3, 2, 1]
    solution = Solution()
    root_node = solution.buildTree(inorder, postorder)
    print(root_node)
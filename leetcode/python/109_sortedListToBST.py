"""
109. 有序链表转换二叉搜索树
中等
给定一个单链表的头节点  head ，其中的元素 按升序排序 ，将其转换为 平衡 二叉搜索树。


示例 1:
-10 -3 0 5 9
      
       0
     /   \
    -3    9
   /     /
 -10    5

输入: head = [-10,-3,0,5,9]
输出: [0,-3,9,-10,null,5]
解释: 一个可能的答案是[0，-3,9，-10,null,5]，它表示所示的高度平衡的二叉搜索树。
示例 2:

输入: head = []
输出: []
 

提示:

head 中的节点数在[0, 2 * 104] 范围内
-105 <= Node.val <= 105


方法一：分治
我们可以直接模拟「前言」部分的构造方案。

具体地，设当前链表的左端点为 left，右端点 right，包含关系为「左闭右开」，
即 left 包含在链表中而 right 不包含在链表中。我们希望快速地找出链表的中位数节点 mid。

为什么要设定「左闭右开」的关系？由于题目中给定的链表为单向链表，访问后继元素十分容易，但无法直接访问前驱元素。
因此在找出链表的中位数节点 mid 之后，如果设定「左闭右开」的关系，我们就可以直接用 (left,mid) 以及 (mid.next,right) 来表示左右子树对应的列表了。
并且，初始的列表也可以用 (head,null) 方便地进行表示，其中 null 表示空节点。

找出链表中位数节点的方法多种多样，其中较为简单的一种是「快慢指针法」。初始时，快指针 fast 和慢指针 slow 均指向链表的左端点 left。
我们将快指针 fast 向右移动两次的同时，将慢指针 slow 向右移动一次，直到快指针到达边界（即快指针到达右端点或快指针的下一个节点是右端点）。
此时，慢指针对应的元素就是中位数。

在找出了中位数节点之后，我们将其作为当前根节点的元素，并递归地构造其左侧部分的链表对应的左子树，以及右侧部分的链表对应的右子树。

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMedian(left: ListNode, right: ListNode) -> ListNode:
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def buildTree(left: ListNode, right: ListNode) -> TreeNode:
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root
        
        return buildTree(head, None)

"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.build_tree(nums, 0, len(nums) - 1)
        
    def build_tree(self, nums, start, end):
        if start > end:
            return
        mid = (start + end) // 2
        root_node = TreeNode(nums[mid])
        root_node.left = self.build_tree(nums, start, mid - 1)
        root_node.right = self.build_tree(nums, mid + 1, end)
        return root_node
    


def gen_link(nums: list):
    if not nums:
        return
    next_node = None
    for i in nums[::-1]:
       cur_node = ListNode(i)
       cur_node.next = next_node
       next_node = cur_node
    return next_node


if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    head = gen_link(nums)
    solution = Solution()
    node = solution.sortedListToBST(head)
    print(node)

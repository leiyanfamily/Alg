"""
2. 两数相加
中等
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
 

提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next





class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.node_to_int(l1)
        n2 = self.node_to_int(l2)
        node_list = [int(i) for i in str(n1 + n2)][::-1]
        return self.list_to_Node(node_list)

    def node_to_int(self, node: Optional[ListNode]):
        num_list = [str(node.val)]
        while node.next:
            num_list.append(str(node.next.val))
            node = node.next
        return int(''.join(num_list[::-1]))
    

    def list_to_Node(self, arr):
        if not arr:
            return
        start_node = ListNode()
        cur_node = start_node
        for i in arr:
            cur_node.next = ListNode(i)
            cur_node = cur_node.next
        return start_node.next
    
class Func1Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 哨兵节点
        carry = 0  # 进位
        while l1 or l2 or carry:  # 有一个不是空节点，或者还有进位，就继续迭代
            if l1:
                carry += l1.val  # 节点值和进位加在一起
                l1 = l1.next  # 下一个节点
            if l2:
                carry += l2.val  # 节点值和进位加在一起
                l2 = l2.next  # 下一个节点
            cur.next = ListNode(carry % 10)  # 每个节点保存一个数位
            carry //= 10  # 新的进位
            cur = cur.next  # 下一个节点
        return dummy.next  # 哨兵节点的下一个节点就是头节点



if __name__ == '__main__':
    solution = Solution()
    l1 = solution.list_to_Node([2,4,3])
    l2 = solution.list_to_Node([5,6,4])
    print(solution.addTwoNumbers(l1, l2))
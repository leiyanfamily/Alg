"""
LCR 147. 最小栈
简单
相关标签
相关企业
请你设计一个 最小栈 。它提供 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。



实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。


示例 1：

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(2);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.stack:
            self.min = min(self.min, x)

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self.min:
            self.min = min(self.stack) if self.stack else float('inf')
        return num

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


class Func1MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minv = float('inf')


    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minv = x
        else:
            self.stack.append(x-self.minv)
            self.minv = min(self.minv,x)


    def pop(self) -> None:
        pop = self.stack.pop()
        if pop < 0:self.minv = self.minv - pop


    def top(self) -> int:
        top = self.stack[-1]
        return self.minv + top if top >= 0 else self.minv


    def getMin(self) -> int:
        return self.minv



if __name__ == '__main__':
    minStack = Func1MinStack()
    minStack.push(-2)
    minStack.push(2)
    minStack.push(-3)
    print(minStack.getMin())  # 返回 - 3.
    print(minStack.pop())
    print(minStack.top())
    print(minStack.getMin())

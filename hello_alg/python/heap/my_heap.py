class MyHeap:

    def __init__(self, nums: list[int]):
        self.max_heap = nums
        for i in range(self.parent(self.size() - 1), -1, -1):
            self.sift_down(i)

    def size(self):
        return len(self.max_heap)

    def left(self, i: int) -> int:
        return 2 * i + 1

    def right(self, i: int) -> int:
        return 2 * i + 2

    def parent(self, i: int) -> int:
        return (i -1) // 2

    def peek(self):
        """访问堆顶元素"""
        return self.max_heap[0]

    def swap(self, i: int, j: int) -> None:
        self.max_heap[i], self.max_heap[j] = self.max_heap[j], self.max_heap[i]

    def is_empty(self) -> bool:
        return self.size() <= 0

    def push(self, val: int):
        """元素入堆"""
        self.max_heap.append(val)
        self.sift_up(self.size() - 1)

    def sift_up(self, i: int):
        """从节点i开始，从底到顶堆化"""
        while True:
            # 获取节点 i 的父节点
            p = self.parent(i)
            # 当越过根节点或节点无需修复时，结束堆化
            if p < 0 or self.max_heap[i] < self.max_heap[p]:
                break
            # 交换两节点
            self.swap(i, p)
            # 循环向上堆化
            i = p

    def pop(self):
        """元素出堆"""
        if self.is_empty():
            raise IndexError('heap is empty')
        # 交换根节点与最右叶节点（交换首元素和尾元素）
        self.swap(0, self.size() - 1)
        # 删除节点
        val = self.max_heap.pop()
        # 从顶至底开始堆化
        self.sift_down(0)
        return val

    def sift_down(self, i: int):
        """从节点i开始，顶至底堆化"""
        while True:
            # 判断节点i,l,r中最大的节点，记为ma
            l, r, ma = self.left(i), self.right(i), i
            if l < self.size() and self.max_heap[ma] < self.max_heap[l]:
                ma = l
            if r < self.size() and self.max_heap[ma] < self.max_heap[r]:
                ma = r
            # 若节点 i 最大或索引 l, r 越界，则无需继续堆化，跳出
            if ma == i:
                break
            # 交换两个节点
            self.swap(i, ma)
            i = ma


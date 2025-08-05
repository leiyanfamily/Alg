"""
Top-k 问题
问题： 给定一个长度为的无序数组 nums ，请返回数组中最大的个元素。

总共执行了
 轮入堆和出堆，堆的最大长度为
 ，因此时间复杂度为
 。该方法的效率很高，当
 较小时，时间复杂度趋向
 ；当
 较大时，时间复杂度不会超过
 。

另外，该方法适用于动态数据流的使用场景。在不断加入数据时，我们可以持续维护堆内的元素，从而实现最大的
 个元素的动态更新。
"""
import heapq


def top_k_heap(nums: list[int], k: int):
    """基于堆查找数组中最大的k个元素"""
    heap = []
    for i in range(k):
        heapq.heappush(heap, nums[i])
    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, nums[i])
    return heap


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(top_k_heap(nums, 3))
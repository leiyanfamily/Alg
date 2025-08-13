"""
位1的个数
给定一个正整数 n，编写一个函数，获取一个正整数的二进制形式并返回其二进制表达式中 设置位 的个数（也被称为汉明重量）。
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(1 for i in range(32) if n & (1 << i))



if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(2147483645))
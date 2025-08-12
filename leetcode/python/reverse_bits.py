"""
颠倒二进制位
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = format(n, '032b')
        binary_item_list = list(binary_str)
        binary_item_list.reverse()
        new_binary_str = ''.join(binary_item_list)
        return int(new_binary_str, 2)



if __name__ == '__main__':
    solution = Solution()
    # print(solution.reverseBits(43261596))

    num = 10
    print(bin(num))
    new_num = num << 1
    print(bin(new_num), new_num)

"""
395. 至少有 K 个重复字符的最长子串

给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。

如果不存在这样的子字符串，则返回 0。

 

示例 1：

输入：s = "aaabb", k = 3
输出：3
解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
示例 2：

输入：s = "ababbc", k = 2
输出：5
解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
 

提示：

1 <= s.length <= 104
s 仅由小写英文字母组成
1 <= k <= 105

遍历所有字符

"""

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_len = 0
        def dfs(start, end):
            nonlocal max_len
            if start > end:
                return
            pos = start
            for i in range(start, end + 1):
                sub_s = s[i]
                if s[start: end + 1].count(sub_s) < k:
                    pos = i
                    break
            else:
                pos = end + 1
            if pos - start > max_len:
                max_len = pos - start
            dfs(pos + 1, end)
        dfs(0, len(s) - 1)
        return max_len
    

if __name__ == "__main__":
    s = "ababacb"
    k = 3
    solution = Solution()
    print(solution.longestSubstring(s, k))

    
            
            



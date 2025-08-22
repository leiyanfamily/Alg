"""
1763. 最长的美好子字符串
简单

提示
当一个字符串 s 包含的每一种字母的大写和小写形式 同时 出现在 s 中，就称这个字符串 s 是 美好 字符串。
比方说，"abABB" 是美好字符串，因为 'A' 和 'a' 同时出现了，且 'B' 和 'b' 也同时出现了。然而，"abA" 不是美好字符串因为 'b' 出现了，而 'B' 没有出现。

给你一个字符串 s ，请你返回 s 最长的 美好子字符串 。如果有多个答案，请你返回 最早 出现的一个。如果不存在美好子字符串，请你返回一个空字符串。

 
示例 1：

输入：s = "YazaAay"
输出："aAa"
解释："aAa" 是一个美好字符串，因为这个子串中仅含一种字母，其小写形式 'a' 和大写形式 'A' 也同时出现了。
"aAa" 是最长的美好子字符串。
示例 2：

输入：s = "Bb"
输出："Bb"
解释："Bb" 是美好字符串，因为 'B' 和 'b' 都出现了。整个字符串也是原字符串的子字符串。
示例 3：

输入：s = "c"
输出：""
解释：没有美好子字符串。
示例 4：

输入：s = "dDzeE"
输出："dD"
解释："dD" 和 "eE" 都是最长美好子字符串。
由于有多个美好子字符串，返回 "dD" ，因为它出现得最早。
 

提示：

1 <= s.length <= 100
s 只包含大写和小写英文字母。
"""

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        """枚举"""
        n = len(s)
        maxPos, maxLen = 0, 0
        for i in range(n):
            lower, upper = 0, 0
            for j in range(i, n):
                if s[j].islower():
                    lower |= 1 << (ord(s[j]) - ord('a'))
                else:
                    upper |= 1 << (ord(s[j]) - ord('A'))
                if lower == upper and j - i + 1 > maxLen:
                    maxPos = i
                    maxLen = j - i + 1
        return s[maxPos: maxPos + maxLen]
    
    def longestNiceSubstring1(self, s: str) -> str:
        maxPos, maxLen = 0, 0
        def dfs(start, end):
            nonlocal maxPos, maxLen
            if start >= end:
                return
            lower, upper = 0, 0
            for i in range(start, end + 1):
                if s[i].islower():
                    lower|= 1 << (ord(s[i]) - ord('a'))
                    print('lower: ', bin(lower)[2:].zfill(26))
                else:
                    upper|= 1 << (ord(s[i]) - ord('A'))
                    print('upper: ', bin(upper)[2:].zfill(26))
            if lower == upper:
                if end - start + 1 > maxLen:
                    maxPos, maxLen = start, end - start + 1
                return
            pos, valid = start, lower & upper
            print('valid: ', bin(valid)[2:].zfill(26))
            while pos <= end:
                start = pos
                while pos <= end and valid & (1 << (ord(s[pos].lower()) - ord('a'))):
                    print('tmp:   ', bin(1 << (ord(s[pos].lower()) - ord('a')))[2:].zfill(26))
                    pos += 1
                dfs(start, pos - 1)
                pos += 1
        dfs(0, len(s) - 1)
        return s[maxPos : maxPos + maxLen]


if __name__ == '__main__':
    s = 'YazaAay'
    solution = Solution()
    # result = solution.longestNiceSubstring(s)
    result = solution.longestNiceSubstring1(s)
    print(result)
"""
3305. 元音辅音字符串计数 I
中等
提示
给你一个字符串 word 和一个 非负 整数 k。

返回 word 的 子字符串 中，每个元音字母（'a'、'e'、'i'、'o'、'u'）至少 出现一次，并且 恰好 包含 k 个辅音字母的子字符串的总数。


示例 1：
输入：word = "aeioqq", k = 1
输出：0
解释：
不存在包含所有元音字母的子字符串。

示例 2：
输入：word = "aeiou", k = 0
输出：1
解释：
唯一一个包含所有元音字母且不含辅音字母的子字符串是 word[0..4]，即 "aeiou"。

示例 3：
输入：word = "ieaouqqieaouqq", k = 1
输出：3
解释：
包含所有元音字母并且恰好含有一个辅音字母的子字符串有：

word[0..5]，即 "ieaouq"。
word[6..11]，即 "qieaou"。
word[7..12]，即 "ieaouq"。

提示：

5 <= word.length <= 250
word 仅由小写英文字母组成。
0 <= k <= word.length - 5
"""


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        """暴力破解"""
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = 0
        for i in range(len(word)):
            occur = set()
            fuyin = 0
            for j in range(i, len(word)):
                if word[j] in vowels:
                    occur.add(word[j])
                else:
                    fuyin += 1
                if len(occur) == 5 and fuyin == k:
                    res += 1
        return res

    def countOfSubstrings2(self, word: str, k: int) -> int:
        """滑动窗口"""
        vowels = {'a', 'e', 'i', 'o', 'u'}

        def count(m: int) -> int:
            n, res, consonants = len(word), 0, 0
            occur = {}
            j = 0
            for i in range(n):
                while j < n and (consonants < m or len(occur) < 5):
                    if word[j] in vowels:
                        occur[word[j]] = occur.get(word[j], 0) + 1
                    else:
                        consonants += 1
                    j += 1
                if consonants >= m and len(occur) == 5:
                    res += n - j + 1
                if word[i] in vowels:
                    occur[word[i]] -= 1
                    if occur[word[i]] == 0:
                        del occur[word[i]]
                else:
                    consonants -= 1
            return res

        return count(k) - count(k + 1)



if __name__ == '__main__':
    word = 'ieaouqqieaouqq'
    # print(Solution().countOfSubstrings(word, 1))
    print(Solution().countOfSubstrings2(word, 1))

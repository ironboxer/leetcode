"""
https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/

395. 至少有K个重复字符的最长子串
找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。

示例 1:

输入:
s = "aaabb", k = 3

输出:
3

最长子串为 "aaa" ，其中 'a' 重复了 3 次。
示例 2:

输入:
s = "ababbc", k = 2

输出:
5

最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            cnt = [0] * 26
            for j in range(i, len(s)):
                cnt[ord(s[j]) - 97] += 1
                for c in cnt:
                    if 0 < c < k:
                        break
                else:
                    res = max(res, j - i + 1)
        return res



# Slow But Work
# 简单有效
from collections import Counter
from functools import lru_cache

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        @lru_cache
        def f(s):
            c = Counter(s)
            for key, val in c.items():
                if val < k:
                    return max(f(item) for item in s.split(key))
            return len(s)

        return f(s)


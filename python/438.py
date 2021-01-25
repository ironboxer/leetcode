"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        pattern = Counter(p)
        memo = Counter()
        lasti, total = 0, 0
        for i, c in enumerate(s):
            if pattern[c] == 0:
                continue
            memo[c] += 1
            if memo[c] == pattern[c]:
                total += 1
            while total == len(pattern) and lasti <= i:
                cc = s[lasti]
                lasti += 1
                if pattern[cc] == 0:
                    continue
                if lasti - 1 + len(p) == i + 1:
                    res.append(lasti - 1)
                memo[cc] -= 1
                if memo[cc] < pattern[cc]:
                    total -= 1

        return res




















class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        from collections import Counter
        need, window = Counter(p), Counter()
        matched, j = 0, 0
        for i, c in enumerate(s):
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    matched += 1
            while i - j + 1 >= len(p):
                if matched == len(need):
                    res.append(j)
                cc = s[j]
                if cc in need:
                    if window[cc] == need[cc]:
                        matched -= 1
                    window[cc] -= 1
                j += 1

        return res


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s, p))

    s = "abab"
    p = "ab"
    print(Solution().findAnagrams(s, p))



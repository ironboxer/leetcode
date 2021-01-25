"""
https://leetcode.com/problems/permutation-in-string/


Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

"""


# TLE
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from itertools import permutations
        for item in permutations(s1):
            if ''.join(item) in s2:
                return True
        return False


# WHAT's the Solution?
# 两个关键词
# 1. 长度相同
# 2. 连续的片段
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        pattern, window = Counter(s1), Counter(s2[:len(s1)])
        if pattern == window:
            return True

        start = 0
        for end, val in enumerate(s2[len(s1):]):
            # add new char
            window[val] += 1

            # delete old char
            c = s2[start]
            window[c] -= 1

            # if didn't delete 0 position, window != pattern
            if window[c] == 0:
                window.pop(c)
            start += 1

            if window == pattern:
                return True

        return False






















class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        need = Counter(s1)
        window = Counter()
        matched = 0
        lasti = 0
        for i, c in enumerate(s2):
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    matched += 1
            # this will shrink the window
            while i - lasti + 1 >= len(s1):
                if matched == len(need):
                    return True
                cc = s2[lasti]
                if cc in need:
                    if window[cc] == need[cc]:
                        matched -= 1
                    window[cc] -= 1
                lasti += 1
        return False



if __name__ == '__main__':
    s1 = "ab"
    s2 = "acccccb"
    print(s1, s2, Solution().checkInclusion(s1, s2))

    s1 = "ab"
    s2 = "eidbaooo"
    print(s1, s2, Solution().checkInclusion(s1, s2))

    s1 = "ab"
    s2 = "eidboaoo"
    print(s1, s2, Solution().checkInclusion(s1, s2))

    s1 = "hello"
    s2 = "ooolleoooleh"
    print(s1, s2, Solution().checkInclusion(s1, s2))

    s1 = "adc"
    s2 = "dcda"
    print(s1, s2, Solution().checkInclusion(s1, s2))

    s1 = "dinitrophenylhydrazine"
    s2 = "acetylphenylhydrazine"
    print(Solution().checkInclusion(s1, s2))

    s1 =     "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef"

    s2 = "bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg"

    print(Solution().checkInclusion(s1, s2))


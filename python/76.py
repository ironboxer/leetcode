"""
https://leetcode.com/problems/minimum-window-substring/

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        c = Counter(t)
        d = Counter()
        matched, total = 0, len(c)
        res, last = None, 0
        for i, e in enumerate(s):
            d[e] += 1
            if d[e] == c[e]:
                matched += 1
                while matched == total and last <= i:
                    if res is None or i - last < res[1] - res[0]:
                        res = (last, i)
                    d[s[last]] -= 1
                    if d[s[last]] < c[s[last]]:
                        matched -= 1
                    last += 1

        return s[res[0]: res[1] + 1] if res else ''











# 这道题还是比较简单而经典的
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        target = Counter(t)
        memo = Counter()
        res = None
        total, lasti = 0, 0
        for i, c in enumerate(s):
            # skip not exists
            if target[c] == 0:
                continue
            memo[c] += 1
            if memo[c] == target[c]:
                total += 1

            while total == len(target) and lasti <= i:
                if res is None:
                    res = (lasti, i)
                elif i - lasti < res[1] - res[0]:
                    res = (lasti, i)

                cc = s[lasti]
                lasti += 1
                # skip not exists
                if target[cc] == 0:
                    continue
                memo[cc] -= 1
                if memo[cc] < target[cc]:
                    total -= 1


        return s[res[0]: res[1] + 1] if res else ''






























class Solution:
    """
    每次做完之后 思路更加清晰
    """
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        need = Counter(t)
        window = Counter()
        res = None
        matched = 0
        j = 0
        for i, c in enumerate(s):
            if not c in need:
                continue
            window[c] += 1
            if window[c] == need[c]:
                matched += 1
                while matched == len(need) and j <= i:
                    if not res or i - j < res[1] - res[0]:
                        res = (j, i)
                    if s[j] in need:
                        if window[s[j]] == need[s[j]]:
                            matched -= 1
                        window[s[j]] -= 1
                    j += 1

        return s[res[0]: res[1] + 1] if res else ''


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))

    s = "a"
    t = "aa"
    print(Solution().minWindow(s, t))

    s = "a"
    t = "a"
    print(Solution().minWindow(s, t))

    s = "bba"
    t = "ab"
    print(Solution().minWindow(s, t))


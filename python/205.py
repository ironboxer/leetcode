"""
https://leetcode.com/problems/isomorphic-strings/
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        p, q = {}, {}
        for a, b in zip(s, t):
            if a in p and p[a] != b or b in q and q[b] != a:
                return False
            p[a] = b
            q[b] = a
        return True


#

if __name__ == '__main__':
    print(Solution().isIsomorphic("egg", "add"))
    print(Solution().isIsomorphic("foo", "bar"))
    print(Solution().isIsomorphic("paper", "title"))
    print(Solution().isIsomorphic("abba", "abab"))
    print(Solution().isIsomorphic("ab", "aa"))

"""
https://leetcode.com/problems/combinations/

"""

from typing import List


class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def f(buf, p):
            if len(buf) == k:
                res.append(buf[:])
                return
            for i in range(p, n + 1):
                buf.append(i)
                f(buf, i + 1)
                buf.pop()

        f([], 1)
        return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return list(combinations(range(1, n + 1), k))


if __name__ == '__main__':
    print(Solution().combine(4, 2))

"""

"""

from typing import List

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                val = A[i] + A[j] + (i - j)
                res = max(res, val)

        return res


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = 0
        mx = A[0] + 0
        for i in range(1, len(A)):
            res = max(res, mx + A[i] - i)
            mx = max(mx, A[i] + i)

        return res


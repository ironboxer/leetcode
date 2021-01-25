"""

"""



# SLOW BUT WORK
# TLE
from typing import List
from itertools import combinations

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        res = 0
        for a, b, c in combinations(A, 3):
            if a + b <= c or a + c <= b or b + c <= a:
                continue
            res = max(res, a + b + c)

        return res





class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        res = 0
        A.sort()
        for i in range(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                res = A[i] + A[i+1] + A[i+2]
                break
        return res




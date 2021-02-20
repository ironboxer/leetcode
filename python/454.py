"""
https://leetcode-cn.com/problems/4sum-ii/

454. 四数相加 II
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""

from typing import List

from collections import Counter

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        c = Counter(i + j for i in A for j in B)
        return sum(c[-i-j] for i in C for j in D)



# SLOW BUT WORK
# TLE
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = [a + b for a in A for b in B]
        CD = [c + d for c in C for d in D]
        return [x + y for x in AB for y in CD].count(0)


# Better Solution
from collections import Counter


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # 统计次数 对于重复的元素 可以大大减小搜索的范围
        AB = Counter(a + b for a in A for b in B)
        # 汇总
        return sum(AB[-c-d] for c in C for d in D)


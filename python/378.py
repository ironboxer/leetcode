"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/


Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.

"""

from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        from heapq import heapify, heappop
        buf = []
        for row in matrix:
            buf.extend(row)
        heapify(buf)

        for i in range(k):
            val = heappop(buf)
        return val

if __name__ == '__main__':
    matrix = [
        [ 1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    print(Solution().kthSmallest(matrix, k))



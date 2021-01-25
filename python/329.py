"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/


Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

"""


from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = {}
        def f(i, j, last):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if matrix[i][j] <= last:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            last = matrix[i][j]
            r = max(f(i+1, j, last), f(i-1, j, last), f(i, j+1, last), f(i, j-1, last)) + 1
            memo[(i, j)] = r
            return r


        return max(f(i, j, -999999) for i in range(m) for j in range(n))


if __name__ == '__main__':
    matrix = [
        [9,9,4],
        [6,6,8],
        [2,1,1]
    ]

    print(Solution().longestIncreasingPath(matrix))

    matrix = [
        [3,4,5],
        [3,2,6],
        [2,2,1]
    ]

    print(Solution().longestIncreasingPath(matrix))

    matrix = [
        [0,1,2,3,4,5,6,7,8,9],
        [19,18,17,16,15,14,13,12,11,10],
        [20,21,22,23,24,25,26,27,28,29],
        [39,38,37,36,35,34,33,32,31,30],
        [40,41,42,43,44,45,46,47,48,49],
        [59,58,57,56,55,54,53,52,51,50],
        [60,61,62,63,64,65,66,67,68,69],
        [79,78,77,76,75,74,73,72,71,70],
        [80,81,82,83,84,85,86,87,88,89],
        [99,98,97,96,95,94,93,92,91,90],
        [100,101,102,103,104,105,106,107,108,109],
        [119,118,117,116,115,114,113,112,111,110],
        [120,121,122,123,124,125,126,127,128,129],
        [139,138,137,136,135,134,133,132,131,130],
        [0,0,0,0,0,0,0,0,0,0]
    ]

    print(Solution().longestIncreasingPath(matrix))



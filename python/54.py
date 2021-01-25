"""
https://leetcode.com/problems/spiral-matrix/

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        m, n = len(matrix), len(matrix[0])
        total = m * n
        row, col = 0, 0
        while len(res) < total:
            if row < m:
                for j in range(col, n):
                    res.append(matrix[row][j])
                row += 1
            if col < n:
                for i in range(row, m):
                    res.append(matrix[i][n - 1])
                n -= 1
            if row < m:
                for j in range(n - 1, col - 1, -1):
                    res.append(matrix[m - 1][j])
                m -= 1
            if col < n:
                for i in range(m - 1, row - 1, -1):
                    res.append(matrix[i][col])
                col += 1

        return res


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(Solution().spiralOrder(matrix))
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(Solution().spiralOrder(matrix))

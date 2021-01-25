"""
https://leetcode.com/problems/spiral-matrix-ii/

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        if n == 0:
            return matrix
        
        counter, total = 1, n * n
        m = n
        row, col = 0, 0
        while counter <= total:
            if row < m:
                for i in range(col, n):
                    matrix[row][i] = counter
                    counter += 1
                row += 1
            if col < n:
                for i in range(row, m):
                    matrix[i][n-1] = counter
                    counter += 1
                n -= 1
            if row < m:
                for i in range(n-1, col-1, -1):
                    matrix[m-1][i]= counter
                    counter += 1
                m -= 1
            if col < n:
                for i in range(m-1, row-1, -1):
                    matrix[i][col] = counter
                    counter += 1
                col += 1
        return matrix


def show(matrix):
    for row in matrix:
        print(row)
    print()

if __name__ == '__main__':
    for i in range(10):
        show(Solution().generateMatrix(i))

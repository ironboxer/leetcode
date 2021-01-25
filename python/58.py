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
import time


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def gen(n):
            for i in range(1, n ** 2 + 1):
                yield i

        board = [[0] * n for _ in range(n)]
        t = n ** 2
        row, col = 0, 0
        m, n = n, n
        it = list(gen(n))
        pos = 0
        while pos < len(it):
            if row < m:
                for i in range(col, n):
                    board[row][i] = it[pos]
                    pos += 1
                row += 1
            if col < n:
                for i in range(row, m):
                    board[i][n - 1] = it[pos]
                    pos += 1
                n -= 1
            if row < m:
                for i in range(n - 1, col - 1, -1):
                    board[m - 1][i] = it[pos]
                    pos += 1
                m -= 1
            if col < n:
                for i in range(m - 1, row - 1, -1):
                    board[i][col] = it[pos]
                    pos += 1
                col += 1

            printBoard(board)
            time.sleep(1)

        return board


def printBoard(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()
    print('-' * 30)


# 简单直白

if __name__ == '__main__':
    for i in range(3, 6):
        board = Solution().generateMatrix(i)
        print(board)

"""
https://leetcode.com/problems/surrounded-regions/

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""

from typing import List


# 不得要领啊, 没有掌握题意啊
# 与border上的0点相连接的O点是不能够被设置为X的,
# 只有那些不与border上相连的O点才能够被设置为X

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        m, n = len(board), len(board[0])

        def f(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if board[i][j] == 'O':
                board[i][j] = 'S'
                f(i + 1, j)
                f(i - 1, j)
                f(i, j - 1)
                f(i, j + 1)

            for i in range(m):
                if board[i][0] == 'O':
                    f(i, 0)
                if board[i][n - 1] == 'O':
                    f(i, n - 1)
            for j in range(n):
                if board[0][j] == 'O':
                    f(0, j)
                if board[m - 1][j] == 'O':
                    f(m - 1, j)

            for i in range(1, m - 1):
                for j in range(1, n - 1):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'

            for i in range(m):
                for j in range(n):
                    if board[i][j] == 'S':
                        board[i][j] = 'O'


if __name__ == '__main__':
    def printBoard(board):
        for row in board:
            for cell in row:
                print(cell, end=' ')
            print()
        print('\n')


    board = [
        ["O", "O", "O"],
        ["O", "O", "O"],
        ["O", "O", "O"]
    ]
    printBoard(board)
    Solution().solve(board)
    printBoard(board)

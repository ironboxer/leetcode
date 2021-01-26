"""
https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.


你所有的不懂都在这
https://zh.wikipedia.org/wiki/%E5%85%AB%E7%9A%87%E5%90%8E%E9%97%AE%E9%A2%98

"""

from typing import List

class Solution:
    """
    整体的思路非常清晰
    唯一难懂的地方就是validate
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        self.dfs(board, 0, res)
        return res

    def dfs(self, board, colIndex, res):
        if colIndex == len(board):
            res.append(["".join(row) for row in board])
            return
        for i in range(len(board)):
            if self.validate(board, i, colIndex):
                board[i][colIndex] = "Q"
                self.dfs(board, colIndex+1, res)
                board[i][colIndex] = "."

    def validate(self, board, x, y):
        for i in range(len(board)):
            for j in range(y):
                if board[i][j] == "Q" and (x + j == y + i or x + y == i + j or x == i):
                    return False
        return True



# SLOW BUT WORK
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def check(board, row, col):
            n = len(board)
            # check row
            # pass

            # check column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # check A
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i, j = i - 1, j - 1

            # check B
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i, j = i - 1, j + 1

            return True

        res = []
        board = [['.'] * n for _ in range(n)]

        def f(row):
            if row == n:
                res.append([''.join(row) for row in board])
                return
            for col in range(n):
                board[row][col] = 'Q'
                if check(board, row, col):
                    f(row+1)
                board[row][col] = '.'

        f(0)

        return res



if __name__ == '__main__':
    for i in range(4, 9):
        boards = Solution().solveNQueens(i)
        for board in boards:
            for row in board:
                print(row)
            print()
        print()

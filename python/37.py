"""
https://leetcode.com/problems/sudoku-solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.

"""

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        def solve(board):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == '.':
                        for c in range(1, 10):
                            if check(board, i, j, str(c)):
                                board[i][j] = str(c)
                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = '.'
                        return False

            return True

        def check(board, row, col, c):
            for i in range(9):
                if board[i][col] != '.' and board[i][col] == c:
                    return False
                if board[row][i] != '.' and board[row][i] == c:
                    return False
                if board[3 * (row//3) + i // 3][3*(col//3) + i % 3] != '.' and \
                        board[3 * (row//3) + i // 3][3*(col//3) + i % 3] == c:
                    return False
            return True

        solve(board)


# ----

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for c in range(1, 10):
                            if check(board, i, j, str(c)):
                                board[i][j] = str(c)
                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = '.'
                        return False

            return True

        def check(board, row, col, c):
            for i in range(9):
                if board[row][i] == c:
                    return False
            for i in range(9):
                if board[i][col] == c:
                    return False

            top, left = row // 3 * 3, col // 3 * 3
            arr = []
            for i in range(3):
                for j in range(3):
                    c = board[top + i][left + j]
                    if c != '.':
                        arr.append(c)

            return len(arr) == len(set(arr))

        solve(board)


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        def check(row, col, val):
            for i in range(9):
                if board[row][i] == val:
                    return False
            for i in range(9):
                if board[i][col] == val:
                    return False
            buf = []
            l, r = row // 3, col // 3
            for i in range(l * 3, (l + 1) * 3):
                for j in range(r * 3, (r + 1) * 3):
                    if board[i][j] != '.':
                        buf.append(board[i][j])

            return len(buf) == len(set(buf))

        def f():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for n in range(1, 10):
                            if check(i, j, str(n)):
                                board[i][j] = str(n)
                                if f():
                                    return True
                                else:
                                    board[i][j] = '.'
                        return False

            # 最后没有.的位置 表示都放对了地方
            return True

        f()




if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    def printBoard(baord):
        for i in range(len(baord)):
            for j in range(len(board[i])):
                print(board[i][j], end=' ')
            print()
        print("\n" * 2)
    printBoard(board)
    Solution().solveSudoku(board)
    printBoard(board)


## 虽然看不懂, 但毕竟抄了一遍.还是不懂啊

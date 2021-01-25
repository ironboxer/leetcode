"""
https://leetcode.com/problems/n-queens-ii/

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0

        def f(board, row):
            if row == n:
                nonlocal res
                res += 1
                return
            for col in range(n):
                if check(board, row, col):
                    board[row][col] = 'Q'
                    f(board, row + 1)
                    board[row][col] = '.'

        # 判重的过程需要好好思考啊
        def check(board, row, col):
            # check column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            # 因为是按照row从小到大来的, 所以row不会超，判断的范围在(0, row)即可
            # 但是col的返回一开始就是从(1, n), 所以每次判断的范文是(0, n)
            # 就是这个原因, 就是这么简单
            # check 45 degree
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i, j = i - 1, j - 1

            # check 135 degree
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i, j = i - 1, j + 1

            return True

        board = [['.'] * n for _ in range(n)]
        f(board, 0)
        return res


if __name__ == '__main__':
    for i in range(4, 11):
        print(i, Solution().totalNQueens(i))

"""
https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, t = len(board), len(board[0]), len(word)
        visited = [[False] * n for _ in range(m)]

        def f(i, j, k):
            if k == t:
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if board[i][j] != word[k]:
                return False
            if visited[i][j]:
                return False
            visited[i][j] = True
            r = f(i + 1, j, k + 1) or \
                f(i, j + 1, k + 1) or \
                f(i - 1, j, k + 1) or \
                f(i, j - 1, k + 1)
            visited[i][j] = False
            return r

        for i in range(m):
            for j in range(n):
                if f(i, j, 0):
                    return True

        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    words = [
        ('ABCCED', True),
        ('SEE', True),
        ('ABCB', False),
    ]
    for word, t in words:
        r = Solution().exist(board, word)
        print(word, t, r)
        assert t == r

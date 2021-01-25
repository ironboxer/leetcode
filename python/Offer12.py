"""
https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/


剑指 Offer 12. 矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。



示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
提示：

1 <= board.length <= 200
1 <= board[i].length <= 200
注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/
"""

from typing import List



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False
        m, n, p = len(board), len(board[0]), len(word)

        def f(i, j, k):
            if k == p:
                return True
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            if board[i][j] != word[k]:
                return False
            t = board[i][j]
            board[i][j] = '#'
            r = f(i+1, j, k+1) or f(i-1, j, k+1) or f(i, j+1, k+1) or f(i, j-1, k+1)
            board[i][j] = t
            return r

        for i in range(m):
            for j in range(n):
                if f(i, j, 0):
                    return True
        return False

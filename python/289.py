"""
https://leetcode.com/problems/game-of-life/


According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

diagonal: 对角线
Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

under-population: 人口不足
over-population: 人口过多
reproduction: 再生产


1. 邻居少于2个会死
2. 邻居2到3个会活到下一轮
3. 邻居多于3个会死
4. 死掉的细胞会活过来,如果邻居恰好有3个是活的

Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

encroaches: 侵害
"""


from typing import List


class Solution:
    def gameOfLifeInfinite(self, live):
        from collections import Counter
        ctr = Counter(
            (I, J) for i, j in live
                   for I in range(i-1, i+2)
                   for J in range(j-1, j+2)
                   if I != i or J != j
        )
        return {ij
                for ij in ctr
                if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

    def gameOfLife(self, board: List[List[int]]) -> None:
        lives = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
        lives = self.gameOfLifeInfinite(lives)
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in lives)


if __name__ == '__main__':

    board =  [
        [0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0]
    ]

    print(board)

    Solution().gameOfLife(board)

    print(board)

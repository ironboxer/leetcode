"""
https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/


1091. 二进制矩阵中的最短路径
在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。

一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成：

相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角）
C_1 位于 (0, 0)（即，值为 grid[0][0]）
C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]）
如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0）
返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。



示例 1：

输入：[[0,1],[1,0]]

输出：2

示例 2：

输入：[[0,0,0],[1,1,0],[1,1,0]]

输出：4



提示：

1 <= grid.length == grid[0].length <= 100
grid[i][j] 为 0 或 1

"""


from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        queue = deque([(0, 0, 1)])
        while queue:
            i, j, v = queue.popleft()
            #print(i, j, v)
            if i + 1 == rows and j + 1 == cols:
                return v
            if visited[i][j]:
                continue
            visited[i][j] = True
            if i + 1 < rows and j + 1 < cols and grid[i+1][j+1] == 0:
                queue.append((i + 1, j + 1, v + 1))
            if i + 1 < rows and grid[i+1][j] == 0:
                queue.append((i + 1, j, v + 1))
            if j + 1 < cols and grid[i][j+1] == 0:
                queue.append((i, j + 1, v + 1))
            if i + 1 < rows and j - 1 >= 0 and grid[i+1][j-1] == 0:
                queue.append((i + 1, j - 1, v + 1))
            if i - 1 >= 0 and j + 1 < cols and grid[i-1][j+1] == 0:
                queue.append((i - 1, j + 1, v + 1))
            if j - 1 >= 0 and grid[i][j-1] == 0:
                queue.append((i, j - 1, v + 1))

        return -1


if __name__ == '__main__':

    grid = [[0,0,1,0,0,0,0],[0,1,0,0,0,0,1],[0,0,1,0,1,0,0],[0,0,0,1,1,1,0],[1,0,0,1,1,0,0],[1,1,1,1,1,0,1],[0,0,1,0,0,0,0]]
    print(Solution().shortestPathBinaryMatrix(grid))

    grid = [[0,0,0,0,1],[1,0,0,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,1,0]]
    print(Solution().shortestPathBinaryMatrix(grid))


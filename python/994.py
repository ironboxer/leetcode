"""
https://leetcode-cn.com/problems/rotting-oranges/

994. 腐烂的橘子
在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。



示例 1：



输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：[[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
示例 3：

输入：[[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。


提示：

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] 仅为 0、1 或 2
"""


from typing import List


from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total, counter = m * n, 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    counter += 1
                    queue.append((i, j, 0))
                elif grid[i][j] == 0:
                    total -= 1

        if counter == total:
            return 0

        max_step = 0
        while queue:
            i, j, step = queue.popleft()
            if counter == total:
                return max_step

            for k in (-1, 1):
                if 0 <= i + k < m and grid[i+k][j] == 1:
                    grid[i+k][j] = 2
                    counter += 1
                    queue.append((i + k, j, step + 1))
                    max_step = max(max_step, step + 1)
                if 0 <= j + k < n and grid[i][j+k] == 1:
                    grid[i][j+k] = 2
                    counter += 1
                    queue.append((i, j + k, step + 1))
                    max_step = max(max_step, step + 1)

        return -1


if __name__ == '__main__':
    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    grid = [[1], [2], [2]]
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    grid = [[0,2]]
    for row in grid:
        print(row)

    print(Solution().orangesRotting(grid))

    for row in grid:
        print(row)


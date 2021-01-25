"""
https://leetcode.com/problems/walls-and-gates/


286. 墙与门
你被给定一个 m × n 的二维网格，网格中有以下三种可能的初始化值：

-1 表示墙或是障碍物
0 表示一扇门
INF 无限表示一个空的房间。然后，我们用 231 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。
你要给每个空房间位上填上该房间到 最近 门的距离，如果无法到达门，则填 INF 即可。

示例：

给定二维网格：

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
运行完你的函数后，该网格应该变成：

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""


from typing import List
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        m, n = len(rooms), len(rooms[0])
        visit = [[False] * n for _ in range(m)]
        max_int = (1 << 31) - 1
        queue = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))
                    visit[i][j] = True
                elif rooms[i][j] == -1:
                    visit[i][j] = True

        while queue:
            i, j, k = queue.popleft()
            rooms[i][j] = k

            for x in (-1, 1):
                ii = i + x
                if ii < 0 or ii >= m or visit[ii][j]:
                    continue
                visit[ii][j] = True
                # if rooms[ii][j] == max_int:
                queue.append((ii, j, k + 1))
            for y in (-1, 1):
                jj = j + y
                if jj < 0 or jj >= n or visit[i][jj]:
                    continue
                visit[i][jj] = True
                # if rooms[i][jj] == max_int:
                queue.append((i, jj, k + 1))



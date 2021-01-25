"""
https://leetcode-cn.com/problems/01-matrix/


542. 01 矩阵
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。



示例 1：

输入：
[[0,0,0],
 [0,1,0],
 [0,0,0]]

输出：
[[0,0,0],
 [0,1,0],
 [0,0,0]]
示例 2：

输入：
[[0,0,0],
 [0,1,0],
 [1,1,1]]

输出：
[[0,0,0],
 [0,1,0],
 [1,2,1]]


提示：

给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。
"""


from typing import List


# TLE slow but work
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        res = [[0] * n for _ in range(m)]
        visit = [[False] * n for _ in range(m)]

        def f(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or visit[i][j]:
                return 999999

            if matrix[i][j] == 0:
                return 0
            visit[i][j] = True
            r = min(f(i-1, j), f(i+1, j), f(i, j-1), f(i, j+1)) + 1
            visit[i][j] = False
            return r

        for i in range(m):
            for j in range(n):
                res[i][j] = f(i, j)

        return res



# slow but work
from queue import PriorityQueue

# 优先队列到的使用 是第一次啊
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        res = [[0] * n for _ in range(m)]
        visit = [[False] * n for _ in range(m)]
        pq = PriorityQueue()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    pq.put((0, i, j))
                    visit[i][j] = True

        while not pq.empty():
            k, i, j = pq.get(block=False)

            res[i][j] = k
            for x in (-1, 1):
                ii = i + x
                if ii < 0 or ii >= m or visit[ii][j]:
                    continue
                pq.put((k+1, ii, j))
                visit[ii][j] = True

            for y in (-1, 1):
                jj = j + y
                if jj < 0 or jj >= n or visit[i][jj]:
                    continue
                pq.put((k+1, i, jj))
                visit[i][jj] = True

        return res


# fast
from collections import deque

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        res = [[0] * n for _ in range(m)]
        visit = [[False] * n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i, j, 0))
                    visit[i][j] = True

        while queue:
            i, j, k = queue.popleft()
            res[i][j] = k
            for x in (-1, 1):
                ii = i + x
                if ii < 0 or ii >= m or visit[ii][j]:
                    continue
                queue.append((ii, j, k+1))
                visit[ii][j] = True

            for y in (-1, 1):
                jj = j + y
                if jj < 0 or jj >= n or visit[i][jj]:
                    continue
                queue.append((i, jj, k+1))
                visit[i][jj] = True

        return res

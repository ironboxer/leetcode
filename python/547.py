"""
https://leetcode-cn.com/problems/friend-circles/
547. 朋友圈
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。



示例 1：

输入：
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出：2
解释：已知学生 0 和学生 1 互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回 2 。
示例 2：

输入：
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出：1
解释：已知学生 0 和学生 1 互为朋友，学生 1 和学生 2 互为朋友，所以学生 0 和学生 2 也是朋友，所以他们三个在一个朋友圈，返回 1 。


提示：

1 <= N <= 200
M[i][i] == 1
M[i][j] == M[j][i]

"""

from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, i):
        v = self.parent[i]
        if v == -1:
            return i
        return self.find(v)

    def union(self, x, y):
        i, j = self.find(x), self.find(y)
        if i != j:
            self.parent[i] = j

    def count(self):
        r = 0
        for i in self.parent:
            if i == -1:
                r += 1
        return r


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        uf = UnionFind(N)
        for i in range(N):
            for j in range(N):
                if M[i][j] == 1 and i != j:
                    uf.union(i, j)
        return uf.count()


if __name__ == '__main__':
    M = [[1,1,0],
         [1,1,0],
         [0,0,1]]

    print(Solution().findCircleNum(M))

    M = [[1,1,0],
         [1,1,1],
         [0,1,1]]

    print(Solution().findCircleNum(M))



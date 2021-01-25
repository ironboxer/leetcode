"""
https://leetcode-cn.com/problems/partition-list/

86. 分隔链表
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。



示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        def bitsum(n):
            r = 0
            while n:
                r += n % 10
                n //= 10
            return r

        visited = [[False] * n for _ in range(m)]

        self.res = 0

        def f(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if bitsum(i) + bitsum(j) > k:
                return
            if visited[i][j]:
                return
            visited[i][j] = True
            self.res += 1
            f(i+1, j)
            f(i-1, j)
            f(i, j+1)
            f(i, j-1)

        f(0, 0)

        return self.res


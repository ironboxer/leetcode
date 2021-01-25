"""
https://leetcode.com/problems/max-points-on-a-line/
"""

from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res, n = 0, len(points)
        for i in range(n):
            dup = 1
            for j in range(i + 1, n):
                cnt = 0
                x1, y1 = points[i]
                x2, y2 = points[j]
                # 给定的集合中存在两个点完全一样
                if x1 == x2 and y1 == y2:
                    dup += 1
                    continue
                for k in range(n):
                    x3, y3 = points[k]
                    # 给定的集合中除去已经选定的两个点, 还有一个点与前面两个点都在一条直线上
                    if x1 * y2 + x2 * y3 + x3 * y1 == x3 * y2 + x2 * y1 + x1 * y3:
                        cnt += 1
                    # 这里, 如果 x3 与前面任意一个点一样
                    # 这样是没有问题的, 因为需要从0开始计算在同一条直线上的点的数量
                    # 所以即便重复了(计算的是相同的点)也没问题(从最终的结果看)
                res = max(res, cnt)
            res = max(res, dup)
        return res

#  这种没有自己理解, 直接抄过来的题 可能永远不懂
# 这个虽然不懂 但是最简单 最容易review

if __name__ == '__main__':
    pass

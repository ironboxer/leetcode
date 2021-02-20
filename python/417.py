"""
https://leetcode-cn.com/problems/pacific-atlantic-water-flow
"""

class Solution(object):
    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        # OPEN 保存待扩展的点
        # CLOSE保存已扩展的点
        # 因为OPEN CLOSE 相互扩展得到 所以不需要维护全部点的 是否已经遍历的集合
        # 每次从OPEN中取出一个点 只要该点不在CLOSE中 就可以添加到OPEN中
        # 因为CLOSE中已经保存了全部已经符合要求的点了
        OPEN = set((x, 0) for x in range(m)) + set((0, y) for y in range(n))
        CLOSE = set()
        while OPEN:
            x, y = OPEN.pop()
            CLOSE.add((x, y))
            if x > 0 and matrix[x][y] <= matrix[x-1][y]:
                if (x-1, y) not in CLOSE:
                    OPEN.add((x-1, y))
            if y > 0 and matrix[x][y] <= matrix[x][y-1]:
                if (x, y-1) not in CLOSE:
                    OPEN.add((x, y-1))
            if x + 1 < m and matrix[x][y] <= matrix[x+1][y]:
                if (x+1, y) not in CLOSE:
                    OPEN.add((x+1, y))
            if y + 1 < n and matrix[x][y] <= matrix[x][y+1]:
                if (x, y+1) not in CLOSE:
                    OPEN.add((x, y+1))
        toPacific = CLOSE

        OPEN = set((x, n-1) for x in range(m)) + set((m-1, y) for y in range(n))
        CLOSE = set()
        while OPEN:
            x, y = OPEN.pop()
            CLOSE.add((x, y))
            if x > 0 and matrix[x][y] <= matrix[x-1][y]:
                if (x-1, y) not in CLOSE:
                    OPEN.add((x-1, y))
            if y > 0 and matrix[x][y] <= matrix[x][y-1]:
                if (x, y-1) not in CLOSE:
                    CLOSE.add((x, y-1))
            if x + 1 < m and matrix[x][y] <= matrix[x+1][y]:
                if (x+1, y) not in CLOSE:
                    OPEN.add((x+1, y))
            if y + 1 < n and matrix[x][y] <= matrix[x][y+1]:
                if (x, y+1) not in CLOSE:
                    OPEN.add((x,y+1))
        toAtlanic = CLOSE

        res = [list(item) for item in toPacific & toAtlanic]
        return res






class Solution:
    """
    将原来的问题拆分为两个子问题 然后求交集
    """
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
            if not matrix or not matrix[0]:
                return []
            m, n = len(matrix), len(matrix[0])

            def f(stack):
                res = set()
                while stack:
                    x, y = stack.pop()
                    res.add((x, y))
                    if x > 0 and (x-1, y) not in res and matrix[x][y] <= matrix[x-1][y]:
                        stack.append((x-1, y))
                    if y > 0 and (x, y-1) not in res and matrix[x][y] <= matrix[x][y-1]:
                        stack.append((x, y-1))
                    if x + 1 < m and (x+1, y) not in res and matrix[x][y] <= matrix[x+1][y]:
                        stack.append((x+1, y))
                    if y + 1 < n and (x, y+1) not in res and matrix[x][y] <= matrix[x][y+1]:
                        stack.append((x, y+1))

                return res

            A = [(i, 0) for i in range(m)] + [(0, j) for j in range(n)]
            B = [(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n)]
            C = f(A) & f(B)
            return [list(item) for item in C]


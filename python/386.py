"""
https://leetcode-cn.com/problems/lexicographical-numbers/

386. 字典序排数
给定一个整数 n, 返回从 1 到 n 的字典顺序。

例如，

给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。

请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。
"""

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1,n+1), key=str)



class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(list(range(1, n+1)), key=str)


# 实际上还有一种更加具体的方式
# 只不过更加的具体了
# 最关键的就是比较函数的确定了

from functools import cmp_to_key

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        def compare(a, b):
            c, d = str(a), str(b)
            if c < d:
                return -1
            if c == d:
                return 0
            return 1


        return sorted(list(range(1, n+1)), key=cmp_to_key(compare))


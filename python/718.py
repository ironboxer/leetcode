"""
https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/


718. 最长重复子数组
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。



示例：

输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。


提示：

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

"""

from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        res = 0

        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1

                res = max(res, dp[i+1][j+1])

        #for row in dp:
        #    print(row)

        return res


# SLOW BUT WORK
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        retval = 0
        m, n = len(A), len(B)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1

                retval = max(retval, dp[i+1][j+1])

        return retval



if __name__ == '__main__':
    A = [0,1,1,1,1]
    B = [1,0,1,0,1]
    print(A)
    print(B)

    print(Solution().findLength(A, B))


    A = [1,2,3,2,1]
    B =  [3,2,1,4,7]
    print(A)
    print(B)

    print(Solution().findLength(A, B))



"""
https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/


673. 最长递增子序列的个数
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。

---

300 单纯的求解最长子序列

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        total = len(nums)
        dp = [1] * (total + 1)
        for i in range(1, total):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


673 在求解最长子序列的基础上 还要求解数量
所以需要保存每个阶段最长子序列的结果

https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/solution/dong-tai-gui-hua-jian-li-shuang-zhong-yi-wei-dpbia/

这是一个很好的思路
"""


from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        total = len(nums)
        dp, comb = [1] * total, [1] * total
        maxval = 1
        for i in range(1, total):
            for j in range(i):
                if nums[i] > nums[j]:
                    # 表示找到了一个更长的单调递增子序列
                    # 所以需要更新dp以及comb
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        comb[i] = comb[j]
                    # 表示由j到i的总的方式
                    elif dp[j] + 1 == dp[i]:
                        comb[i] += comb[j]
            maxval = max(maxval, dp[i])

        return sum(comb[j] for i, e in enumerate(dp) if e == maxval)


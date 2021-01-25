"""
https://leetcode-cn.com/problems/k-concatenation-maximum-sum/

1191. K 次串联后最大子数组之和
给你一个整数数组 arr 和一个整数 k。

首先，我们要对该数组进行修改，即把原数组 arr 重复 k 次。

举个例子，如果 arr = [1, 2] 且 k = 3，那么修改后的数组就是 [1, 2, 1, 2, 1, 2]。

然后，请你返回修改后的数组中的最大的子数组之和。

注意，子数组长度可以是 0，在这种情况下它的总和也是 0。

由于 结果可能会很大，所以需要 模（mod） 10^9 + 7 后再返回。



示例 1：

输入：arr = [1,2], k = 3
输出：9
示例 2：

输入：arr = [1,-2,1], k = 5
输出：2
示例 3：

输入：arr = [-1,-2], k = 7
输出：0


提示：

1 <= arr.length <= 10^5
1 <= k <= 10^5
-10^4 <= arr[i] <= 10^4

"""

# Common Solution
# TLE

from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        nums = arr * k
        total = len(nums)
        if total == 0:
            return 0
        dp = [0] * (total + 1)
        for i, e in enumerate(nums):
            if dp[i] > 0:
                dp[i+1] += dp[i] + e
            else:
                dp[i+1] = e
        return max(dp) % (10 ** 9 + 7)


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        total, s = len(arr), sum(arr)
        cur, res = 0, 0
        loop = min(2, k) * total
        for i in range(loop):
            val = arr[i % total]
            cur = max(cur + val, 0)
            res = max(res, cur)
        if s > 0:
            while k > 2:
                res += s
                k -= 1

        return res % (10 ** 9 + 7)

# https://leetcode-cn.com/problems/k-concatenation-maximum-sum/solution/java-kadanesuan-fa-yu-jie-ti-si-lu-by-zdxiq125/

if __name__ == '__main__':
    arr = [1,-2,1]
    k = 5
    print(Solution().kConcatenationMaxSum(arr, k))

    arr = [1,0,4,1,4]
    k = 4
    print(Solution().kConcatenationMaxSum(arr, k))

    arr = [1,-2,1]
    k = 5
    print(Solution().kConcatenationMaxSum(arr, k))


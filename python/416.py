"""
https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

---

与494. 目标和 类似，属于01背包问题，可以把问题抽象为“给定一个数组和一个容量为x的背包，求有多少种方式让背包装满（有多少种子集能让子集之和等于背包容量）?"
递推公式：dp[i] = dp[i] + dp[i-num] ，对于当前的第i个物品，有拿和不拿两种情况，dp[i]表示不拿的情况，dp[i-num]表示拿的情况，因此要将两者相加。

class Solution {
    public boolean canPartition(int[] nums) {
        int len = nums.length;
        int sum = 0;
        for (int n : nums) {
            sum += n;
        }
        if(sum % 2 != 0) return false;//整数相加不可能得小数
        int W = sum / 2;//相当于背包总承重
        int [] dp = new int[W+1];
        dp[0] = 1;
        for (int num : nums) {
            for (int i = W; i >= num; i--) {
                dp[i] += dp[i-num];
            }
        }
        return dp[W] != 0;
    }
}

01 背包就是每件物品只能拿一次非0即1
完全背包就是每件物品可以拿n次

附上01背包问题的模版：

//01背包
for (int i = 0; i < n; i++) {
    for (int j = m; j >= V[i]; j--) {
        f[j] = max(f[j], f[j-V[i]] + W[i]);
    }
}
//完全背包
for (int i = 0; i < n; i++) {
    for (int j = V[i]; j <= m; j++) {
        f[j] = max(f[j], f[j-V[i]] + W[i]);
    }
}
f[j]代表当前背包容量为j的时候，可以获取的最大价值。完全背包是从左向右遍历，f[j-V[i]]取到的是拿第i个物品时的值，是新值，可以重复无限的拿，f[j]的值也会随之增加。
V：商品的体积
W：商品的价值

"""


from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if bool(s & 1):
            return False

        s //= 2
        n = len(nums)
        # 在集合中找到一半的元素 使得和为s
        dp = [[False] * (s + 1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, s + 1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

        return dp[n][s]

























class Solution:
     def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        # odd case
        if s // 2 * 2 != s:
            return False

        nums.sort()
        memo = {}
        def f(s, i):
            val = memo.get(s)
            if val is not None:
                return val
            if s == 0:
                val = True
                memo[s] = val
                return val
            if i == len(nums):
                val = False
                memo[s] = val
                return val
            for j in range(i, len(nums)):
                n = nums[i]
                if n > s:
                    break
                if f(s - n, j + 1) or f(s, j + 1):
                    val = True
                    memo[s] = val
                    return val
            val = False
            memo[s] = val
            return val

        return f(s // 2, 0)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if (s >> 1) << 1 != s:
            return False
        s >>= 1
        n = len(nums)
        dp = [[False] * (s + 1) for _ in range(n + 1)]
        # 这里的初始化非常关键 表示 sum==0时为true
        for i in range(n+1):
            dp[i][0] = True
        for i in range(n):
            # j表示重量 应该从1开始才是有意义的
            for j in range(1,s + 1):
                if nums[i] <= j:
                    dp[i+1][j] = dp[i][j-nums[i]] or dp[i][j]
                else:
                    dp[i+1][j] = dp[i][j]
        for row in dp:
            print(row)
        return dp[n][s]



# SLOW BUT WORK
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False
        s >>= 1

        def f(pos, cur):
            if cur == s:
                return True
            if pos == len(nums):
                return False
            for i in range(pos, len(nums)):
                if cur + nums[i] > s:
                    continue
                r = f(i + 1, cur + nums[i])
                if r:
                    return True

            return False

        return f(0, 0)


# Using DP

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return 0
        s >>= 1
        dp = [0] * (s + 1)
        for i in nums:
            for j in range(s, i-1, -1):
                dp[j] = max(dp[j], dp[j-i] + i)

        return dp[s] == s


if __name__ == '__main__':
    nums = [1,5,11,5]
    print(Solution().canPartition(nums))

    nums = [1,2,3,5]
    print(Solution().canPartition(nums))


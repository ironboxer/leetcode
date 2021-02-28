"""
https://leetcode-cn.com/problems/maximum-profit-in-job-scheduling/


1235. 规划兼职工作
你打算利用空闲时间来做兼职工作赚些零花钱。

这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。

给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。

注意，时间上出现重叠的 2 份工作不能同时进行。

如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。



示例 1：



输入：startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
输出：120
解释：
我们选出第 1 份和第 4 份工作，
时间范围是 [1-3]+[3-6]，共获得报酬 120 = 50 + 70。
示例 2：



输入：startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
输出：150
解释：
我们选择第 1，4，5 份工作。
共获得报酬 150 = 20 + 70 + 60。
示例 3：



输入：startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
输出：6


提示：

1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4

"""

from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        if n == 0:
            return 0

        times = list(zip(startTime, endTime, profit))
        times.sort(key=lambda x: x[1])
        prev_list = [-1] * n
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if times[i][0] >= times[j][1]:
                    prev_list[i] = j
                    break

        opt_list = [0] * n
        for i in range(0, n):
            opt_list[i] = max(opt_list[i-1], opt_list[prev_list[i]] + times[i][2])

        return opt_list[-1]


class Solution:
    def jobScheduling(self, s: List[int], e: List[int], p: List[int]) -> int:
        n=len(s)
        arr=[]
        for i in range(n):
            arr.append([s[i],e[i],p[i]])

        arr.sort(key=lambda x:x[1])
        arr=[[0,0,0]]+arr
        dp=[0]*(n+1)
        for i in range(1,n+1):
            l,r=0,i-1
            while l<r:
                mid=l+(r-l+1)//2
                if arr[mid][1]<=arr[i][0]:
                    l=mid
                else:
                    r=mid-1
            # dp[i]表示第i个以arr[i]结尾的子序列的最大值
            dp[i]=max(dp[i-1],dp[r]+arr[i][2])

        return dp[-1]


# 二分查找 + 动态规划 求最优解吗?
# 这道题做了还是不会啊 明显感觉到 有很多细节没有搞明白啊
# 这道题本质上就是一个动态规划
# 其中的状态转移方程 为 f(i) = max(f(i-1), f(j) + arr[i][2]) if arr[j][1] <= arr[i][0]
# 0 <= j < i < len(arr) 其中j是第一个小于i且满足 arr[j][1] <= arr[i][0]的位置
# 至于说 这里使用二分查找 还是 普通的线性查找 都是关于查找的具体算法
# 但是 本质上还是动态规划类 题目
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        total = len(startTime)
        arr = [[0, 0, 0]] + sorted(list(zip(startTime, endTime, profit)), key=lambda x: x[1])
        dp = [0] * (total + 1)
        for i in range(1, total + 1):
            j = i - 1
            while j > 0 and arr[j][1] > arr[i][0]:
                j -= 1
            dp[i] = max(dp[i-1], dp[j] + arr[i][2])

        return dp[-1]



if __name__ == '__main__':

    startTime = [1,1,1]
    endTime = [2,3,4]
    profit = [5,6,4]

    print(Solution().jobScheduling(startTime, endTime, profit))

    startTime = [1,2,3,4,6]
    endTime = [3,5,10,6,9]
    profit = [20,20,100,70,60]

    print(Solution().jobScheduling(startTime, endTime, profit))

    startTime = [1,2,3,3]
    endTime = [3,4,5,6]
    profit = [50,10,40,70]

    print(Solution().jobScheduling(startTime, endTime, profit))



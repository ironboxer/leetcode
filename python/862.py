"""
https://leetcode-cn.com/problems/shortest-subarray-with-sum-at-least-k/


862. 和至少为 K 的最短子数组
返回 A 的最短的非空连续子数组的长度，该子数组的和至少为 K 。

如果没有和至少为 K 的非空子数组，返回 -1 。



示例 1：

输入：A = [1], K = 1
输出：1
示例 2：

输入：A = [1,2], K = 4
输出：-1
示例 3：

输入：A = [2,-1,2], K = 3
输出：3


提示：

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
通过次数10,610提交次数64,612
在真实的面试中遇到过这道题？
"""


from typing import List


def bsearch(nums, target):
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) >> 1
        if nums[m][0] > target:
            r = m
        else:
            l = m + 1

    return l



class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        retval = 1 << 31
        s = 0
        stack = [(0, - 1)]
        for i, e in enumerate(A):
            s += e
            # 说明当前的e一定是个负数
            # 保持stack是一个单调递增栈
            # 但是这样 栈中的元素就不在连续
            while stack and stack[-1][0] >= s:
                stack.pop()
            # 查找prev节点的位置
            j = bsearch(stack, s - K)
            if j > 0:
                # 如果存在该节点 则更新
                # 注意这里的二分查找算法 有稍微的改动
                # 会优先返回最右边符合条件的结果
                retval = min(retval, i - stack[j-1][1])

            stack.append((s, i))

        return retval if retval < 1 << 31 else -1


if __name__ == '__main__':
    A = [44,-25,75,-50,-38,-42,-32,-6,-40,-47]
    K = 19
    print(A, K)
    print(Solution().shortestSubarray(A, K))


    A = [84,-37,32,40,95]
    K = 167
    print(A, K)
    print(Solution().shortestSubarray(A, K))



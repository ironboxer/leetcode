"""
https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/

剑指 Offer 10- II. 青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
示例 3：

输入：n = 0
输出：1
提示：

0 <= n <= 100
注意：本题与主站 70 题相同：https://leetcode-cn.com/problems/climbing-stairs/


"""


class Solution:
    def numWays(self, n: int) -> int:
        a, b = 0, 1
        for i in range(1, n+1):
            a, b = b, a + b
        return b % 1000000007


if __name__ == '__main__':
    for i in range(0, 50):
        print(i, Solution().numWays(i))


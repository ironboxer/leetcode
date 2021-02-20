"""
https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/

剑指 Offer 62. 圆圈中最后剩下的数字
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。



示例 1：

输入: n = 5, m = 3
输出: 3
示例 2：

输入: n = 10, m = 17
输出: 2


限制：

1 <= n <= 10^5
1 <= m <= 10^6
"""

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        res = 0
        for i in range(2, n+1):
            res = (res + m) % i
        return res


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        retval = 0
        nums = list(range(n))
        while n > 1:
            retval = (retval + m - 1) % n
            nums.pop(retval)
            n -= 1
        return nums[0]


if __name__ == '__main__':
    n = 5
    m = 2
    print(Solution().lastRemaining(n, m))


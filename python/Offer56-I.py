"""
https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/

剑指 Offer 56 - I. 数组中数字出现的次数
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。



示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]


限制：

2 <= nums.length <= 10000

"""

from typing import List


class Solution:
    """
    这道题的基本原理是什么?
    """
    def singleNumbers(self, nums: List[int]) -> List[int]:
        r = 0
        for n in nums:
            r ^= n
        x = r & -r
        a, b = 0, 0
        for n in nums:
            if x & n:
                a ^= n
            else:
                b ^= n
        return [a, b]



class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        s = 0
        for n in nums:
            s ^= n
        # a ^ b = s
        # s & -s 是找到s的最低位的1表示的数字
        mask = s & -s
        # 用mask来划分a, b两个数字
        # 其中的一个数字在mask的位上满足 mask & a == 1
        # 而另外一个数字在mask的位上满足 mask & b == 0
        # 因为mask = s & -s 所以说明在最低位上两个数字a, b就是不同的 一个为1 一个为0
        # 所以可以使用mask来划分这两个数字
        a, b = 0, 0
        for n in nums:
            # 这里考察了 ^ 异或运算满足交换律
            if mask & n:
                a ^= n
            else:
                b ^= n

        return [a, b]


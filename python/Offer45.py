"""
https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/

剑指 Offer 45. 把数组排成最小的数
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。



示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"


提示:

0 < nums.length <= 100
说明:

输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
"""

from typing import List


from functools import cmp_to_key


def compare(a, b):
    return int(str(a) + str(b)) - int(str(b) + str(a))


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums.sort(key=cmp_to_key(compare))
        print(nums)
        return ''.join(map(str, nums))


if __name__ == '__main__':
    nums = [9, 5, 34, 30, 3]
    print(nums)
    print(Solution().minNumber(nums))

    nums = [1,2,3,4,5,6,7,8,9,0]
    print(nums)
    print(Solution().minNumber(nums))



"""
https://leetcode-cn.com/problems/nth-digit/


400. 第 N 位数字
在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 位数字。



注意：n 是正数且在 32 位整数范围内（n < 231）。



示例 1：

输入：3
输出：3
示例 2：

输入：11
输出：0
解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。


---
解题思路

1   ~   9：区间包含9个正整数，每个正整数包含一个数字，共9*1个数字
10  ~  99：区间包含90个正整数，每个正整数包含两个数字，共90*2个数字
100 ~ 999：区间包含900个正整数，每个正整数包含三个数字，共900*3个数字
参数定义
num：当前区间整数个数，如9,90,900……
cnt：当前区间正整数包含数字的个数，如整数123，则cnt=3
target：目标正整数，即查找的第n位数字在正整数target中
index：查找结果在整数target中的第几位
思路
获取第n位所在区间。比如n=200，通过计算可知，200-9*1-90*2=11，即包含第n个数字的正整数在100~999这个区间，且在100,101,102,103中的第11位
计算目标数。100~999区间每个正整数由三个数字构成，由于100相当于从0开始，计算下标为(11-1)//3=3，则目标数target=100+3=103
计算答案在目标数的第几位。index=11%3=2，即103中的第二位为0。由于数组中下标从0开始，则index=(11-1)%3=1，str(target)[index]即为所求。
复杂度分析
时间复杂度：O(1)，时间复杂度与区间个数有关，因为n是正数且在32位整数范围内，2^31-1=2147483647，区间最多为10个。
空间复杂度：O(1)

作者：yim-6
链接：https://leetcode-cn.com/problems/nth-digit/solution/python3-di-nge-shu-zi-by-yim-6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

#这里的解法都是有原因的


class Solution:
    def findNthDigit(self, n: int) -> int:
        num = 9
        cnt = 1

        while n > num * cnt:
            n -= num * cnt
            num *= 10
            cnt += 1

        target = num // 9 + (n - 1) // cnt
        index = (n - 1) % cnt
        print(num, cnt, n, target, index)
        return str(target)[index]


if __name__ == '__main__':
    for i in range(22):
        print(i, Solution().findNthDigit(i))


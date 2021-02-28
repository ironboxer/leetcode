"""
https://leetcode-cn.com/problems/greatest-sum-divisible-by-three/


1262. 可被三整除的最大和
给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。



示例 1：

输入：nums = [3,6,5,1,8]
输出：18
解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
示例 2：

输入：nums = [4]
输出：0
解释：4 不能被 3 整除，所以无法选出数字，返回 0。
示例 3：

输入：nums = [1,2,3,4,4]
输出：12
解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。


提示：

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4

---

先求出数组的和，然后求出和模上3的数字(minus)，模一共有三种情况：
1.总和模为0直接返回，即所有数相加可以被3整除。
2.总和模为1，然后找到一个最小的模为1的数和两个最小模为2的数的和，和减去其中的最小值，如果和最后小于0返回0否则返回和的值。
3.总和模为2，然后找到一个最小的模为2的数和两个最小模为1的数的和，和减去其中的最小值，如果和最后小于0返回0否则返回和的值。

作者：xun-luo
链接：https://leetcode-cn.com/problems/greatest-sum-divisible-by-three/solution/xian-qiu-chu-shu-zu-he-zai-jian-qu-shu-z-me0i/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


# slow but work


from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        res = 0

        def f(pos, buf):
            val = sum(buf)
            if val % 3 == 0:
                nonlocal res
                res = max(res, val)

            if pos == len(nums):
                return

            for i in range(pos, len(nums)):
                buf.append(nums[i])
                f(i+1, buf)
                buf.pop()

        f(0, [])

        return res


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        if total % 3 == 0:
            return total
        minus = total % 3
        t1 = m1 = m2 = 1 << 31
        for n in nums:
            if n % 3 == minus:
                t1 = min(t1, n)
            elif n % 3 != 0:
                # suppose m2 < m1
                if n < m2:
                    m1 = m2
                    m2 = n
                elif n < m1:
                    m1 = n

        total -= min(t1, m1 + m2)

        return total if total else 0


if __name__ == '__main__':

    nums = [3,6,5,1,8]
    print(Solution().maxSumDivThree(nums))


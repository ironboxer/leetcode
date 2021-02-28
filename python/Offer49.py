"""
https://leetcode-cn.com/problems/chou-shu-lcof/

剑指 Offer 49. 丑数
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。



示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:

1 是丑数。
n 不超过1690。
注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        a, b, c = 0, 0, 0
        while len(nums) < n:
            while nums[a] * 2 <= nums[-1]:
                a += 1
            while nums[b] * 3 <= nums[-1]:
                b += 1
            while nums[c] * 5 <= nums[-1]:
                c += 1
            nums.append(min(nums[a] * 2, nums[b] * 3, nums[c] * 5))

        return nums[-1]


"""
func min(a, b int) int {
    if a <= b {
        return a
    }
    return b
}

func min3(a, b, c int) int {
    return min(min(a, b), c)
}


func nthUglyNumber(n int) int {
    var a, b, c int
    var res = make([]int, n)
    res[0] = 1
    for i := 1; i < n; i++ {
        for res[a] * 2 <= res[i-1] {
            a++
        }
        for res[b] * 3 <= res[i-1] {
            b++
        }
        for res[c] * 5 <= res[i-1] {
            c++
        }
        res[i] = min3(res[a] * 2, res[b] * 3, res[c] * 5)
    }
    return res[n-1]
}
"""

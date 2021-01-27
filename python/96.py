"""
https://leetcode.com/problems/unique-binary-search-trees/

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


Constraints:

1 <= n <= 19

keep my knees
卡特兰数
F(i, n) = G(i-1) * G(n-i)
"""


class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n + 1)
        G[0] = G[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[n]


class Solution:
    nums = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190]

    def numTrees(self, n: int) -> int:
        return self.nums[n]



# 这里有一个简单的公式可以参考
# 而且比较好记
class Solution:
    def numTrees(self, n: int) -> int:
        if n < 2:
            return 1
        r = 1
        for i in range(2, n+1):
            r = r * (4 * i - 2) // (i + 1)

        return r


if __name__ == '__main__':
    pass

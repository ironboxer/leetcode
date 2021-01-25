"""
https://leetcode.com/problems/permutation-sequence/

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

https://leetcode.com/problems/permutation-sequence/discuss/22512/Share-my-Python-solution-with-detailed-explanation

"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        nums = [str(i) for i in range(1, n + 1)]
        res = ''
        k -= 1
        while n > 0:
            n -= 1
            i, k = divmod(k, math.factorial(n))
            res += nums[i]
            nums.pop(i)

        return res


# 这样的解法


# slow but work

from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        gen = permutations(list(range(1,n+1)))
        r = None
        for _ in range(k):
            r = next(gen)
        return ''.join([str(i) for i in r])


if __name__ == '__main__':
    print(Solution().getPermutation(3, 3))
    print(Solution().getPermutation(3, 5))
    print(Solution().getPermutation(4, 1))

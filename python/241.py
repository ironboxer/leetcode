"""
https://leetcode.com/problems/different-ways-to-add-parentheses/

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
"""


from typing import List

# 这是一个非常好的题

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        import re, operator
        tokens = re.split(r'(\D)', input)
        nums = [int(i) for i in tokens[::2]]
        ops = tokens[1::2]
        M = {'+': operator.add, '-': operator.sub, '*': operator.mul}

        def build(low, high):
            if low == high:
                return [nums[low]]
            res = []
            # ops nums之间有某种对应关系
            for i in range(low, high):
                a = build(low, i)
                b = build(i+1, high)
                #tmp = [M[ops[i]](p, q) for p in a for q in b]
                #print(a, ops[i], b, tmp)
                res.extend([M[ops[i]](p, q) for p in a for q in b])
            return res

        return build(0, len(nums) - 1)


if __name__ == '__main__':
    print(Solution().diffWaysToCompute("2*3-4*5"))



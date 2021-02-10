"""

"""



from typing import List



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0

        for n in nums:
            seen_once = ~seen_twice & (seen_once ^ n)
            seen_twice = ~seen_once & (seen_twice ^ n)

        return seen_once


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        A, B = 0, 0
        for n in nums:
            C = B & n
            B = (B & ~n) | (A & n)
            A = A ^ n
            A &= ~C

        return A


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        A, B = 0, 0
        for n in nums:
            A = ~B & (A ^ n)
            B = ~A & (B ^ n)
        return A


if __name__ == '__main__':
    nums = [3,3,3,2,2,2,1]
    print(Solution().singleNumber(nums))



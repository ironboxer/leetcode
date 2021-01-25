"""
https://leetcode.com/problems/summary-ranges/

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

"""

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        buf = []
        last = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if nums[i-1] != last:
                    buf.append((last, nums[i-1]))
                else:
                    buf.append(last)
                last = nums[i]

        if last < nums[-1]:
            buf.append((last, nums[-1]))
        elif last == nums[-1]:
            buf.append(last)
        res = []
        for item in buf:
            if isinstance(item, int):
                res.append(str(item))
            else:
                res.append(f'{item[0]}->{item[1]}')
        return res


if __name__ == '__main__':
    nums = [0,1,2,4,5,7]
    print(Solution().summaryRanges(nums))
    nums = [0,2,3,4,6,8,9]
    print(Solution().summaryRanges(nums))


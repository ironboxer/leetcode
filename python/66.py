"""
https://leetcode.com/problems/plus-one/

Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9

"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        v = 1
        for i in range(len(digits) - 1, -1, -1):
            r = digits[i] + v
            digits[i] = r % 10
            v = r // 10

        if v:
            digits.insert(0, v)
        return digits

if __name__ == '__main__':
    digits = [1,2,3]
    print(Solution().plusOne(digits))
    digits = [4,3,2,1]
    print(Solution().plusOne(digits))
    digits = [9]
    print(Solution().plusOne(digits))

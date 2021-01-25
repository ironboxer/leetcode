"""
https://leetcode.com/problems/h-index-ii/

Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had
             received 0, 1, 3, 5, 6 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?

"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        A = citations
        while A and A[0] < len(A):
            A = A[1:]
        return len(A)


# a new quick version


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        A = citations
        total = len(A)
        left, right = 0, len(A)
        while left < right:
            mid = (left + right) // 2
            if A[mid] >= total - mid:
                right = mid
            else:
                left = mid + 1

        return total - left


if __name__ == '__main__':
    print(Solution().hIndex([0,1,3,5,6]))


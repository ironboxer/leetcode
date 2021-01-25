"""
https://leetcode.com/problems/corporate-flight-bookings/


1109. Corporate Flight Bookings
Medium

555

105

Add to List

Share
There are n flights, and they are labeled from 1 to n.

We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

Return an array answer of length n, representing the number of seats booked on each flight in order of their label.



Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]


Constraints:

1 <= bookings.length <= 20000
1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
1 <= bookings[i][2] <= 10000

"""


from typing import List



class Solution:
    """
    TLE
    """
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        for i, j, v in bookings:
            # NOTE: slow
            for k in range(i-1, j):
                res[k] += v
        return res


class Difference:
    def __init__(self, nums):
        assert nums
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i-1]

    def increment(self, i, j, val):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    def result(self):
        res = [0] * len(self.diff)
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i-1] + self.diff[i]
        return res


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = Difference([0] * n)
        for i, j, v in bookings:
            diff.increment(i-1, j-1, v)

        return diff.result()


if __name__ == '__main__':
    bookings = [
        [1,2,10],
        [2,3,20],
        [2,5,25]
    ]
    n = 5
    print(Solution().corpFlightBookings(bookings, n))


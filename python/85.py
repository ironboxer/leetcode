"""
https://leetcode.com/problems/maximal-rectangle/

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.



Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = []
Output: 0
Example 3:

Input: matrix = [["0"]]
Output: 0
Example 4:

Input: matrix = [["1"]]
Output: 1
Example 5:

Input: matrix = [["0","0"]]
Output: 0


Constraints:

rows == matrix.length
cols == matrix.length
0 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        left = [0] * n
        right = [n - 1] * n
        height = [0] * n
        for i in range(m):
            rb = n - 1
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], rb)
                else:
                    right[j] = n - 1
                    rb = j - 1
            lb = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], lb)
                    height[j] += 1
                    max_area = max(max_area, height[j] * (right[j] - left[j] + 1))
                else:
                    height[j] = 0
                    left[j] = 0
                    lb = j + 1

        return max_area


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    # 这里的清零非常重要
                    heights[j] = 0
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        heights = [0, *heights, 0]
        stack = []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                j = stack.pop()
                max_area = max(max_area, (i - stack[-1] - 1) * heights[j])
            stack.append(i)
        return max_area


# a better Solution


if __name__ == '__main__':
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(Solution().maximalRectangle(matrix))

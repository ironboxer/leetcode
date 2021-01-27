"""
https://leetcode.com/problems/largest-rectangle-in-histogram/

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.




Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].




The largest rectangle is shown in the shaded area, which has area = 10 unit.



Example:

Input: [2,1,5,6,2,3]
Output: 10

class Solution {
    /*
    这个题的核心是要保持一个单调递增的stack，每次遇到比栈顶小的元素，pop掉最高的元素
    此时最高的元素是局部最小的height，这里就需要利用当前i的index减去栈顶前一个元素的坐标
    这样可以得到这个局部的width是多少。这样height*width就是局部最小的面积。

    如果当前的i仍然大于栈顶元素，继续进行pop，这样得到下一个局部最小值

    最后stack剩下的height index，就是全局下最小的index，因为比他们大的，都被pop掉了
    所以直接pop stack，width就是总的len 减去他的index即可

    */
    public int largestRectangleArea(int[] heights) {
        if (heights == null || heights.length == 0)
            return 0;

        Stack<Integer> stack = new Stack();

        int len = heights.length;
        int maxArea = Integer.MIN_VALUE;

        for (int i=0;i<len;i++) {

            while (!stack.isEmpty() && heights[i] < heights[stack.peek()]) {
                int partialMaxArea = heights[stack.pop()] * (i - (stack.isEmpty()?0:stack.peek()+1));
                maxArea = Math.max(maxArea, partialMaxArea);
            }

            stack.push(i);
        }

        while (!stack.isEmpty()){
            int partialMaxArea = heights[stack.pop()] * (len - (stack.isEmpty()?0:stack.peek()+1));
            maxArea = Math.max(maxArea, partialMaxArea);
        }

        return maxArea;
    }
}
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [-1]
        heights.append(0)
        # heights最后一个元素是0, 所以前面的元素一定会被计算到
        for i, h in enumerate(heights):
            while h < heights[stack[-1]]:
                # print(stack)
                H = heights[stack.pop()]
                W = i - stack[-1] - 1
                max_area = max(max_area, H * W)
            stack.append(i)
        return max_area


# 这道题并没有真正的搞明白
# 为什么用stack的方式是可行的?

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack = []
        length = len(heights)
        max_area = 0
        for i in range(length):
            while stack and heights[i] < heights[stack[-1]]:
                area = heights[stack.pop()] * (i - (heights[stack[-1]] + 1 if stack else 0))
                max_area = max(max_area, area)

            stack.append(i)

        while stack:
            area = heights[stack.pop()] * (i - (heights[stack[-1]] + 1 if stack else 0))
            max_area = max(max_area, area)

        return max_area




class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        # 所谓的单调栈 就是维护了一个高度 自增(非严格)的序列
        # 然后计算这个序列中的最大高度(最右边)和最大宽度(最左边)
        stack = [-1]
        heights.append(0)
        for i, h in enumerate(heights):
            while h < heights[stack[-1]]:
                H = heights[stack.pop()]
                W = i - stack[-1] - 1
                max_area = max(max_area, W * H)
            stack.append(i)

        return max_area


# 还是下面这个算法更简单
# 但是两者的思路都是一样的
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        # 所谓的单调栈 就是维护了一个高度 自增(非严格)的序列
        # 然后计算这个序列中的最大高度(最右边)和最大宽度(最左边)
        stack = [-1]
        heights.append(0)
        for i, h in enumerate(heights):
            while h < heights[stack[-1]]:
                H = heights[stack.pop()]
                W = i - stack[-1] - 1
                max_area = max(max_area, W * H)
            stack.append(i)

        return max_area


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    print(Solution().largestRectangleArea(heights))

    heights = [10, 5]
    print(Solution().largestRectangleArea(heights))

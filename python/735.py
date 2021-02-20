"""
https://leetcode-cn.com/problems/asteroid-collision/


735. 行星碰撞
给定一个整数数组 asteroids，表示在同一行的行星。

对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。

找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。



示例 1：

输入：asteroids = [5,10,-5]
输出：[5,10]
解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。
示例 2：

输入：asteroids = [8,-8]
输出：[]
解释：8 和 -8 碰撞后，两者都发生爆炸。
示例 3：

输入：asteroids = [10,2,-5]
输出：[10]
解释：2 和 -5 发生碰撞后剩下 -5 。10 和 -5 发生碰撞后剩下 10 。
示例 4：

输入：asteroids = [-2,-1,1,2]
输出：[-2,-1,1,2]
解释：-2 和 -1 向左移动，而 1 和 2 向右移动。 由于移动方向相同的行星不会发生碰撞，所以最终没有行星发生碰撞。


提示：

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""


from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # 只有栈顶元素是正数 当前元素是负数 这种情况 才需要判断
            # 因为两者的方向相交了 但是只有在 abs(n) > abs(stack[-1])
            # 的情况下才弹出栈 表示 栈顶元素被抵消了
            while stack and 0 < stack[-1] < -a:
                stack.pop()
            # 入栈的条件
            # 1 当前栈是空的
            # 栈顶的元素是负数 表示 栈顶向左
            # 当前元素是正数 表示向右
            if not stack or stack[-1] < 0 or a > 0:
                stack.append(a)
            # 如果栈顶元素向右 而 当前元素向左 且两者的值相等 则抵消掉
            elif -a == stack[-1]:
                stack.pop()

        return stack


if __name__ == '__main__':
    nums = [-1, 1]
    print(nums, Solution().asteroidCollision(nums))


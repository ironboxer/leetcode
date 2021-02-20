"""
https://leetcode-cn.com/problems/remove-k-digits/

402. 移掉K位数字
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

注意:

num 的长度小于 10002 且 ≥ k。
num 不会包含任何前导零。
示例 1 :

输入: num = "1432219", k = 3
输出: "1219"
解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
示例 2 :

输入: num = "10200", k = 1
输出: "200"
解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
示例 3 :

输入: num = "10", k = 2
输出: "0"
解释: 从原数字移除所有的数字，剩余为空就是0。
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        total = len(num)

        self.r = ''

        def f(pos, buf):
            if len(buf) == k:
                t = ''.join([e for i, e in enumerate(num) if i not in buf])
                if not self.r or self.r > t:
                    self.r = t
                return

            for i in range(pos, total):
                buf.add(i)
                f(i + 1, buf)
                buf.discard(i)

        f(0, set())

        return self.r.lstrip('0') or '0'

#TLE

# 其实很简单 维护一个最小的滑动窗口 如果有小于当前栈顶元素的新的元素
# 就将栈顶的元素pop出来
# 最终得到到序列就是移除k个元素之后最小的序列了
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []
        for c in num:
            while stack and k > 0 and c < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(c)
        if k > 0:
            stack = stack[:-k]
        return ''.join(stack).lstrip('0') or '0'


if __name__ == '__main__':
     num = "1432219"
     k = 3
     print(Solution().removeKdigits(num, k))


"""
https://leetcode-cn.com/problems/longest-repeating-character-replacement/v

424. 替换后的最长重复字符
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意:
字符串长度 和 k 不会超过 104。

示例 1:

输入:
s = "ABAB", k = 2

输出:
4

解释:
用两个'A'替换为两个'B',反之亦然。
示例 2:

输入:
s = "AABABBA", k = 1

输出:
4

解释:
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。
"""


from collections import Counter


class Solution:
    """
    这道题的思路就是维护一个满足条件的窗口 window
    每次添加一个元素 就检查当前窗口是否满足条件
    如果不满足条件 就删除最早进入窗口的元素
    条件: max(window.values()) + k < i - j + 1
    如果该条件成立 说明当前窗口中的元素不重复的数量已经超过运行的范围k个
    所以就需要从中删除不满足条件的元素
    又因为最后的结果需要是一个连续的序列 所以只需要删除最左侧的元素即可

    总结的过程就是收敛的过程 就是下结论 定型的过程 限制
    """
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        j = 0
        window = Counter()
        for i, e in enumerate(s):
            window[e] += 1
            while max(window.values()) + k < i - j + 1:
                window[s[j]] -= 1
                j += 1
            res = max(res, i - j + 1)

        return res


"""
https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/

剑指 Offer 48. 最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。



示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


提示：

s.length <= 40000
注意：本题与主站 3 题相同：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        lasti = 0
        window = {}
        for i, e in enumerate(s):
            j = window.get(e, -1)
            while lasti <= j:
                window.pop(s[lasti])
                lasti += 1
            window[e] = i
            res = max(res, len(window))
        return res


# 优化 不需要弹出元素 只做标记就行
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        lasti = 0
        window = {}
        for i, e in enumerate(s):
            j = window.get(e, -1)
            if j != -1:
                # lasti的更新需要注意 必须要比较一下大小 总是选择最大的
                lasti = max(lasti, j + 1)
            res = max(res, i - lasti + 1)
            window[e] = i
        return res


if __name__ == '__main__':
    s = 'abba'
    print(Solution().lengthOfLongestSubstring(s))


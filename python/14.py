"""
https://leetcode-cn.com/problems/longest-common-prefix/

14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n < 1:
            return ''
        if n == 1:
            return strs[0]
        min_len = min(len(s) for s in strs)
        for i in range(min_len):
            for j in range(n-1):
                if strs[j][i] != strs[j+1][i]:
                    return strs[j][:i]

        return strs[0][:min_len]


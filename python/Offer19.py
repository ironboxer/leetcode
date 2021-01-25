"""
https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/


请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。
注意：本题与主站 10 题相同：https://leetcode-cn.com/problems/regular-expression-matching/



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @lru_cache
        def f(i, j):
            if j == n:
                return i == m
            if i == m:
                return f(i, j+2) if j + 1 < n and p[j+1] == '*' else False
            if j + 1 < n and p[j+1] == '*':
                if s[i] == p[j] or p[j] == '.':
                    return f(i+1, j) or f(i+1, j+2) or f(i, j+2)
                else:
                    return f(i, j+2)
            if s[i] == p[j] or p[j] == '.':
                return f(i+1, j+1)
            return False

        return f(0, 0)



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _  in range(m + 1)]
        dp[-1][-1] = True
        for i in range(m, -1, -1):
            for j in range(n-1, -1, -1):
                if j + 1 < n and p[j+1] == '*':
                    if i < m and (s[i] == p[j] or p[j] == '.'):
                        dp[i][j] = dp[i+1][j] or dp[i+1][j+2] or dp[i][j+2]
                    else:
                        dp[i][j] = dp[i][j+2]
                elif i < m and (s[i] == p[j] or p[j] == '.'):
                   dp[i][j] = dp[i+1][j+1]

        return dp[0][0]


if __name__ == '__main__':
    cases = [
        ["aa", "a", False],
        ["aa", "a*", True],
        ["ab", ".*", True],
        ["aab", "c*a*b", True],
        ["mississippi", "mis*is*p*.", False],
    ]

    for a, b, c in cases:
        r = Solution().isMatch(a, b)
        print(a, b, c, r)
        assert c == r


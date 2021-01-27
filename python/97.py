"""
https://leetcode-cn.com/problems/interleaving-string/

97. 交错字符串
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
提示：a + b 意味着字符串 a 和 b 连接。



示例 1：


输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true
示例 2：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false
示例 3：

输入：s1 = "", s2 = "", s3 = ""
输出：true


提示：

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1、s2、和 s3 都由小写英文字母组成
"""





from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        @lru_cache
        def f(s1, s2, s3):
            if not s3:
                return not s1 and not s2
            if not s1 and not s2:
                return False
            if not s1:
                return s2[0] == s3[0] and f(s1, s2[1:], s3[1:])
            if not s2:
                return s1[0] == s3[0] and f(s1[1:], s2, s3[1:])

            a, b = False, False
            if s1[0] == s3[0]:
                a = f(s1[1:], s2, s3[1:])
            if s2[0] == s3[0]:
                b = f(s1, s2[1:], s3[1:])
            return a or b

        return f(s1, s2, s3)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, p = len(s1), len(s2), len(s3)

        @lru_cache
        def f(i, j, k):
            if k == p:
                return i == m and j == n
            if i == m and j == n:
                return False
            if i == m:
                return s2[j] == s3[k] and f(i, j+1, k+1)
            if j == n:
                return s1[i] == s3[k] and f(i+1, j, k+1)

            a, b = False, False
            if s1[i] == s3[k]:
                a = f(i+1, j, k+1)
            if s2[j] == s3[k]:
                b = f(i, j+1, k+1)
            return a or b

        return f(0, 0, 0)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, p = len(s1), len(s2), len(s3)

        if m + n != p:
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] |= dp[i-1][0]
        for j in range(1, n + 1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] |= dp[0][j-1]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i-1][j]
                if s2[j-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i][j-1]

        return dp[-1][-1]


from functools import lru_cache

# SLOW BUT WORK
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, p = len(s1), len(s2), len(s3)
        if m + n != p:
            return False

        @lru_cache
        def f(s1, s2, s3):
            if s1 + s2 == s3:
                return True
            if not s3:
                return s1 + s2 == ''
            a = b = False
            if s1 and s1[0] == s3[0]:
                a = f(s1[1:], s2, s3[1:])
            if s2 and s2[0] == s3[0]:
                b = f(s1, s2[1:], s3[1:])

            return a or b

        return f(s1, s2, s3)



from functools import lru_cache


# DP不要忘记备忘录模式
# 因为这是最好理解的一种解题思路啊
# 动态规划难在哪里呢?
# 如何应对呢?
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, p = len(s1), len(s2), len(s3)
        if m + n != p:
            return False

        @lru_cache
        def f(s1, s2, s3):
            if s1 + s2 == s3:
                return True
            if not s3:
                return s1 + s2 == ''
            # 注意这里是或的关系
            # 有可能 s1[0] == s3[0] s2[0] == s3[0]
            # 所以两者都需要保留啊
            a = b = False
            if s1 and s1[0] == s3[0]:
                a = f(s1[1:], s2, s3[1:])
            if s2 and s2[0] == s3[0]:
                b = f(s1, s2[1:], s3[1:])

            return a or b

        return f(s1, s2, s3)

# DP 完全不会 每次全靠CV

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, p = len(s1), len(s2), len(s3)
        if m + n != p:
            return False
        dp = [[False] * (n + 1) for _ in range(m+1)]
        # 表示 s1 == s2 == s3 == '' 为真
        dp[0][0] = True
        for i in range(1, m+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] |= dp[i-1][0]
        for j in range(1, n+1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] |= dp[0][j-1]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i-1][j]
                if s2[j-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i][j-1]

        return dp[-1][-1]


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(Solution().isInterleave(s1, s2, s3))

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    print(Solution().isInterleave(s1, s2, s3))

    s1 = "cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc"
    s2 = "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb"
    s3 = "abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb"

    print(Solution().isInterleave(s1, s2, s3))


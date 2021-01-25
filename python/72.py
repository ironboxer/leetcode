"""
https://leetcode.com/problems/edit-distance/

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""


class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def f(a, b):
            if not a and not b:
                return 0
            if not a:
                return len(b)
            if not b:
                return len(a)
            key = (len(a), len(b))
            if key in memo:
                return memo[key]
            if a[0] == b[0]:
                v = f(a[1:], b[1:])
                memo[key] = v
                return v
            v = min(
                f(a, b[1:]),
                f(a[1:], b),
                f(a[1:], b[1:])
            ) + 1
            memo[key] = v
            return v

        return f(word1, word2)


class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = {}
        def f(i, j):
            if i == m and j == n:
                return 0
            if i == m:
                return n - j
            if j == n:
                return m - i
            key = (i, j)
            if key in memo:
                return memo[key]
            if word1[i] == word2[j]:
                val = f(i+1, j+1)
                memo[key] = val
                return val
            val = min(f(i+1, j), f(i, j+1), f(i+1, j+1)) + 1
            memo[key] = val
            return val

        return f(0, 0)


class Solution:
    """这个反而是最慢的"""
    def minDistance(self, word1: str, word2: str) -> int:
        #如何处理边界问题
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m and j == n:
                    pass
                elif i == m:
                    dp[i][j] = dp[i][j+1] + 1
                elif j == n:
                    dp[i][j] = dp[i+1][j] + 1
                else:
                    if word1[i] == word2[j]:
                        dp[i][j] = dp[i+1][j+1]
                    else:
                        dp[i][j] = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) + 1

        return dp[0][0]


























class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def f(a, b):
            key = (a, b)
            val = memo.get(key)
            if val is not None:
                return val
            if not a:
                val = len(b)
                memo[key] = val
                return val
            if not b:
                val = len(a)
                memo[key] = val
                return val
            if a[0] == b[0]:
                val = f(a[1:], b[1:])
                memo[key] = val
                return val
            val = min(f(a[1:], b), f(a, b[1:]), f(a[1:], b[1:])) + 1
            memo[key] = val
            return val

        return f(word1, word2)



class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 这个初始化极为重要
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1
        return dp[m][n]


if __name__ == '__main__':
    word1 = ""
    word2 = "hello"
    print(Solution().minDistance(word1, word2))
    print('\n')


    word1 = "horse"
    word2 = "ros"
    print(Solution().minDistance(word1, word2))
    print('\n')

    word1 = "intention"
    word2 = "execution"
    print(Solution().minDistance(word1, word2))
    print('\n')

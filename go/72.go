/*

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

*/

package main


import "fmt"


func min(a, b int) int {
    if a <= b {
        return a
    }
    return b
}


func min3(a, b, c int) int {
    return min(min(a, b), c)
}


// 建模 抽象
/*
func minDistance(word1 string, word2 string) int {
    m, n := len(word1), len(word2)
    dp := make([][]int, m + 1)
    for i := 0; i < m + 1; i++ {
        dp[i] = make([]int, n + 1)
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if word1[i] == word2[j] {
                dp[i+1][j+1] = dp[i][j]
            } else {
                dp[i+1][j+1] = min3(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
            }
        }
    }
    fmt.Println(dp)
    return dp[m][n]
}
*/

/*
func minDistance(word1 string, word2 string) int {
    memo := make(map[[2]int]int, 0)
    m, n := len(word1), len(word2)
    var f func(i, j int) int
    f = func(i, j int) int {
        if i == m {
            return n - j
        }
        if j == n {
            return m - i
        }
        key := [2]int{i, j}
        val, ok := memo[key]
        if ok {
            return val
        }
        if word1[i] == word2[j] {
            val = f(i+1, j+1)
            memo[key] = val
            return val
        }
        val = min3(f(i+1, j), f(i, j+1), f(i+1, j+1)) + 1
        memo[key] = val
        return val
    }
    return f(0, 0)
}
*/

/*

[0 0 0 5]
[0 0 0 4]
[0 0 0 3]
[0 0 0 2]
[0 0 0 1]
[3 2 1 0]

[0 0 0 0 0 0 0 0 0 9]
[0 0 0 0 0 0 0 0 0 8]
[0 0 0 0 0 0 0 0 0 7]
[0 0 0 0 0 0 0 0 0 6]
[0 0 0 0 0 0 0 0 0 5]
[0 0 0 0 0 0 0 0 0 4]
[0 0 0 0 0 0 0 0 0 3]
[0 0 0 0 0 0 0 0 0 2]
[0 0 0 0 0 0 0 0 0 1]
[9 8 7 6 5 4 3 2 1 0]

需要做一种类似这样的填充 意思是:
当word1 == '' 或者 word2 == '' 时
table应该有的初始化
**/

func minDistance(word1 string, word2 string) int {
    m, n := len(word1), len(word2)
    dp := make([][]int, m + 1)
    for i := 0; i < m + 1; i++  {
        dp[i] = make([]int, n + 1)
    }
    for i := m; i >= 0; i-- {
        for j := n; j >= 0; j-- {
            // right corner border
            if i == m && j == n {
                dp[i][j] = 0    
            // word2 shorter then word1
            } else if i == m {
                dp[i][j] = dp[i][j+1] + 1
            // word1 shorted then word2
            } else if j == n {
                dp[i][j] = dp[i+1][j] + 1
            } else {
                if word1[i] == word2[j] {
                    dp[i][j] = dp[i+1][j+1]
                } else {
                    dp[i][j] = min3(dp[i+1][j+1], dp[i+1][j], dp[i][j+1]) + 1
                }
            }
        }
    }
    for _, row := range dp {
        fmt.Println(row)
    }
    return dp[0][0]
}


func main() {
    word1 := "horse"
    word2 := "ros"
    fmt.Println(minDistance(word1, word2))

    word1 = "intention"
    word2 = "execution"
    fmt.Println(minDistance(word1, word2))
}

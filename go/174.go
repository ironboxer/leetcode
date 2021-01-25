/*


https://leetcode.com/problems/dungeon-game/

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.



Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)


Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

*/


package main


import "fmt"


func min(a, b int) int {
    if a <= b {
        return a
    }
    return b
}


func calculateMinimumHP(dungeon [][]int) int {
    m, n := len(dungeon), len(dungeon[0])
    dp := make([][]int, m + 1)
    for i := 0; i < m + 1; i++ {
        dp[i] = make([]int, n + 1)
        for j := 0; j < n + 1; j++ {
            dp[i][j] = int((2 << 30) - 1)
        }
    }
    // 为什么这里要初始化为1?
    dp[m][n-1] = 1
    dp[m-1][n] = 1
    for i := m - 1; i >= 0; i-- {
        for j := n - 1; j >= 0; j-- {
            // 首先 left-top 依赖 right-buttom的结果
            // 如果need <= 0 说明 right-buttom 是正数 不需要 "弥补" 所以当前位置设一个最小值1就可以
            // 如果need >  0 说明 right0buttom 是负数 需要得到 "弥补", 而弥补的值就是 need
            need := min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
            if need <= 0 {
                // 为什么这里又要设置为1?
                dp[i][j] = 1
            } else {
                dp[i][j] = need
            }
        }
    }
    // 1是被允许的最小的数字 因为要大于0才可以
    return dp[0][0]
}


func main() {
    dungeon := [][]int {
        {-2, -3, 3},
        {-5, -10, 1},
        {10, 30, -5},
    }
    fmt.Println(calculateMinimumHP(dungeon))
}

/*

https://leetcode.com/problems/climbing-stairs/

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

*/

package main


import "fmt"


func climbStairs(n int) int {
    a, b := 0, 1
    for i := 0; i < n; i++ {
        a, b = b, a + b
    }
    return b
}


func main() {
    for i := 1; i < 46; i++ {
        fmt.Println(i, climbStairs(i))
    }
}

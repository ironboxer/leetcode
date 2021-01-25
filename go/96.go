/*

https://leetcode.com/problems/unique-binary-search-trees/

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


Constraints:

1 <= n <= 19

*/

// 卡特兰数
// F(i, n) = G(i-1) * G(n-i)

package main


import "fmt"


func numTrees(n int) int {
    G := make([]int, n + 1)
    G[0], G[1] = 1, 1
    for i := 2; i <= n; i++ {
        for j := 1; j <= i; j++ {
            G[i] += G[j - 1] * G[i - j]
        }
    }
    return G[n]
}


func main() {
    for i := 2; i < 19; i++ {
        fmt.Println(i, numTrees(i))
    }
}

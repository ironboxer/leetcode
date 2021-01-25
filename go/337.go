/*

https://leetcode.com/problems/house-robber-iii/

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

*/


package main


import "fmt"


type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}



/*
func max(a, b int) int {
    if a >= b {
        return a
    }
    return b
}


// according to definiation
func rob(root *TreeNode) int {
    dict := make(map[*TreeNode]int)
    var f func(root *TreeNode) int
    f = func(root *TreeNode) int {
        if root == nil {
            return 0
        }
        
        val, ok := dict[root]
        if ok {
            return val
        }
        if root.Left != nil {
            val = val + f(root.Left.Left) + f(root.Left.Right)
        }
        if root.Right != nil {
            val = val + f(root.Right.Left) + f(root.Right.Right)
        }
        t := max(root.Val + val, f(root.Left) + f(root.Right))
        dict[root] = t
        return t
    }
    return f(root)
}
*/

func max(nums ...int) int {
    val := nums[0]
    for i := 1; i < len(nums); i++ {
        if nums[i] > val {
            val = nums[i]
        }
    }
    return val
}


func rob(root *TreeNode) int {
    var f func(root *TreeNode) []int
    f = func(root *TreeNode) []int {
        if root == nil {
            return []int{0, 0}
        }
        a, b := f(root.Left), f(root.Right)
        // sub tree node val                 cur node val
        return []int{max(a...) + max(b...), root.Val + a[0] + b[0]}
    }
    return max(f(root)...)
}



func main() {
    var root *TreeNode = nil
    root = &TreeNode{3, nil, nil}
    root.Left = &TreeNode{4, nil, nil}
    root.Right = &TreeNode{5, nil, nil}
    root.Left.Left = &TreeNode{1, nil, nil}
    root.Left.Right = &TreeNode{3, nil, nil}
    root.Right.Right = &TreeNode{1, nil, nil}

    fmt.Println(rob(root))
}


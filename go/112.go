/*

https://leetcode.com/problems/path-sum/

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

*/


package main


import "fmt"

/**
 * Definition for a binary tree node.
 */


type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}


func hasPathSum(root *TreeNode, sum int) bool {
    isNull := func(root *TreeNode) bool {
        return root == nil
    }
    isLeaf := func(root *TreeNode) bool {
        return root != nil && root.Left == nil && root.Right == nil
    }
    var f func(root *TreeNode, val int) bool
    f = func(root *TreeNode, val int) bool {
        if isNull(root) {
            return false
        }
        val = val + root.Val
        if isLeaf(root) {
            return val == sum
        }
        return f(root.Left, val) || f(root.Right, val)
    }
    if root == nil {
        return false
    }
    return f(root, 0)
}


func main() {
    root := &TreeNode{Val: 1, Left: nil, Right: nil}
    root.Left = &TreeNode{Val: 2, Left: nil, Right: nil}
    fmt.Println(hasPathSum(root, 1))
}


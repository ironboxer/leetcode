/*

https://leetcode.com/problems/path-sum-ii/

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]


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


func pathSum(root *TreeNode, sum int) [][]int {
    res := make([][]int, 0)
    isNull := func(root *TreeNode) bool {
        return root == nil
    }
    isLeaf := func(root *TreeNode) bool {
        return root != nil && root.Left == nil && root.Right == nil
    }
    var f func(root *TreeNode, val int, buf []int)
    f = func(root *TreeNode, val int,  buf[]int) {
        if isNull(root) {
            return
        }
        val = val - root.Val
        buf = append(buf, root.Val)
        if isLeaf(root) && val == 0 {
            tmp := make([]int, len(buf)) 
            copy(tmp, buf)
            res = append(res, tmp)
            return
        }
        f(root.Left, val, buf)
        f(root.Right, val, buf)
    }
    buf := make([]int, 0)
    f(root, sum, buf)
    return res
}


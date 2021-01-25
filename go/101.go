/*

https://leetcode.com/problems/symmetric-tree/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

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


func isSymmetric(root *TreeNode) bool {
    var f func(a, b *TreeNode) bool 
    f = func(a, b *TreeNode) bool {
        if a == nil && b == nil {
            return true
        }
        if a == nil && b != nil || b == nil && a != nil {
            return false
        }
        if a.Val != b.Val {
            return false
        }
        return f(a.Left, b.Right) && f(a.Right, b.Left)
    }
    if root == nil {
        return true
    }
    return f(root.Left, root.Right)
}


func main() {

}

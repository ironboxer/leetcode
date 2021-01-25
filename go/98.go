/*

https://leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

*/


package main


import "fmt"


// Definition for a binary tree node.
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

 
/*
func isValidBST(root *TreeNode) bool {
    nums := make([]int, 0)
    
    var f func(root *TreeNode)
    f = func(root *TreeNode) {
        if root != nil {
            f(root.Left)
            nums = append(nums, root.Val)
            f(root.Right)
        }
    }
    f(root)

    for i := 0; i < len(nums) - 1; i++ {
        if nums[i] >= nums[i+1] {
            return false
        }
    }
    return true
}
*/


/*
func isValidBST(root *TreeNode) bool {
    var lasti *int = nil
    retval := true  
    var f func(root *TreeNode)
    f = func(root *TreeNode) {
        if root != nil {
            f(root.Left)
            if lasti == nil {
                lasti = &root.Val
            } else {
                if root.Val <= *lasti {
                    retval = false
                    return
                }
            }
            lasti = &root.Val
            f(root.Right)
        }
    }
    f(root)
    return retval
}
*/



func isValidBST(root *TreeNode) bool {
    var lasti *int = nil

    var f func(root *TreeNode) bool
    f = func(root *TreeNode) bool {
        if root == nil {
            return true
        }
        if f(root.Left) == false {
            return false
        }
        if lasti == nil {
            lasti = &root.Val
        } else if root.Val <= *lasti {
            return false
        }
        lasti = &root.Val
        return f(root.Right)
    }
    return f(root)
}



func main() {
    root := &TreeNode{Val: 2, Left: nil, Right: nil}
    root.Left = &TreeNode{Val: 1, Left: nil, Right: nil}
    root.Right = &TreeNode{Val: 3, Left: nil, Right: nil}

    res := isValidBST(root)
    fmt.Println(res)

    root = &TreeNode{Val: -2147483648, Left: nil, Right: nil}
    res = isValidBST(root)
    fmt.Println(res)

}

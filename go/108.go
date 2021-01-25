/*

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/


Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

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


func sortedArrayToBST(nums []int) *TreeNode {
    var f func(nums []int) *TreeNode
    f = func(nums []int) *TreeNode {
        if len(nums) == 0 {
            return nil
        }
        mid := len(nums) / 2
        root := &TreeNode{Val: nums[mid], Left: nil, Right: nil}
        root.Left = f(nums[:mid])
        root.Right = f(nums[mid+1:])
        return root
    }

    return f(nums) 
}



func inorder(root *TreeNode) {
    if root == nil {
        return
    }
    inorder(root.Left)
    fmt.Println(root.Val)
    inorder(root.Right)
}

func main() {
    nums := []int{0,1,2,3,4,5,6,7,8,9}
    root := sortedArrayToBST(nums)
    inorder(root)
}

/*

https://leetcode.com/problems/binary-tree-paths/

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

*/


package main


import "fmt"
import "strconv"


type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}


// 很简单的一道题 就是二叉树的基本定义
func binaryTreePaths(root *TreeNode) []string {
    res := make([]string, 0)
    isNull := func(root *TreeNode) bool {
        return root == nil
    }
    isLeaf := func(root *TreeNode) bool {
        return root != nil && root.Left == nil && root.Right == nil
    }
    var f func(root *TreeNode, path string)
    f = func(root *TreeNode, path string) {
        if isNull(root) {
            return
        }
        if len(path) == 0 {
            path = strconv.Itoa(root.Val)
        } else {
            path = path + "->" + strconv.Itoa(root.Val)
        }
        if isLeaf(root) {
            res = append(res, path)
            return
        }
        f(root.Left, path)
        f(root.Right, path)
    }
    f(root, "")
    return res
}


func main() {
    var root *TreeNode = nil
    root = &TreeNode{1, nil, nil}
    root.Left = &TreeNode{2, nil, nil}
    root.Right = &TreeNode{3, nil, nil}
    root.Left.Right = &TreeNode{5, nil, nil}
    fmt.Println(binaryTreePaths(root))
}

/*

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

*/


package main


import "fmt"


type TreeNode struct {
    Val   int
    Left  *TreeNode
    Right *TreeNode
}


func isSubTree(root, node *TreeNode) bool {
    if root != nil {
        if root == node {
            return true
        }
        return isSubTree(root.Left, node) || isSubTree(root.Right, node)
    }
    return false
}


func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    var f func(root, p, q *TreeNode) *TreeNode
    f = func(root, p, q *TreeNode) *TreeNode {
        if root == p || root == q {
            return root
        }
        if isSubTree(p, q) {
            return p
        }
        if isSubTree(q, p) {
            return q
        }
        if isSubTree(root.Left, p) && isSubTree(root.Left, q) {
            return f(root.Left, p, q)
        }
        if isSubTree(root.Right, p) && isSubTree(root.Right, q) {
            return f(root.Right, p, q)
        }
        return root
    }
    return f(root, p, q)
}


func main() {
    var root *TreeNode = nil
    root = &TreeNode{6, nil, nil}
    root.Left = &TreeNode{2, nil, nil}
    root.Right = &TreeNode{8, nil, nil} 
    root.Left.Left = &TreeNode{0, nil, nil}
    root.Left.Right = &TreeNode{4, nil, nil}
    root.Left.Right.Left = &TreeNode{3, nil, nil}
    root.Left.Right.Right = &TreeNode{5, nil, nil}
    root.Right.Left = &TreeNode{7, nil, nil}
    root.Right.Right = &TreeNode{9, nil, nil}
    
    fmt.Println(lowestCommonAncestor(root, root.Left.Left, root.Left.Right.Left))
    fmt.Println(lowestCommonAncestor(root, root.Left.Right.Left, root.Right.Left))
    fmt.Println(lowestCommonAncestor(root, root.Left, root.Left.Right.Right))
}

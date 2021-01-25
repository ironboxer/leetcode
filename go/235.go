/*

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


Constraints:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.

*/


package main


import "fmt"


type TreeNode struct {
    Val   int
    Left  *TreeNode
    Right *TreeNode
}


/*
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    var f func(root, p, q *TreeNode) *TreeNode
    f = func(root, p, q *TreeNode) *TreeNode {
        if root == p || root == q {
            return root
        }
        if q.Val < p.Val {
            p, q = q, p
        }
        // assume p.Val < q.Val
        if p.Val < root.Val && root.Val < q.Val {
            return root
        }
        if q.Val < root.Val {
            return f(root.Left, p, q)
        }
        if p.Val > root.Val {
            return f(root.Right, p, q)
        }
        return nil
    }

    return f(root, p, q)
}
*/


// 根据二叉树的定义
// 思路变得十分简单
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    for root != nil {
        if p.Val > root.Val && q.Val > root.Val {
            root = root.Right
        } else if q.Val < root.Val && p.Val < root.Val {
            root = root.Left
        } else {
            break
        }
    }
    return root
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

/*

https://leetcode.com/problems/minimum-depth-of-binary-tree/


Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

*/


/**
 * Definition for a binary tree node.
 */

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}


/*
需要仔细读一下题意 很容易出错
*/
func minDepth(root *TreeNode) int {

    min := func(a, b int) int {
        if a <= b {
            return a
        }
        return b
    }

    isLeaf := func(node *TreeNode) bool {
        return node != nil && node.Left == nil && node.Right == nil
    }

    isNull := func(node *TreeNode) bool {
        return node == nil
    }

    var f func(root *TreeNode) int
    f = func(root *TreeNode) int {
        if isNull(root) {
            return 999999
        }
        if isLeaf(root) {
            return 1
        }
        return min(f(root.Left), f(root.Right)) + 1
    }
    
    depth := f(root)
    if depth >= 999999 {
        return 0
    }
    return depth
}

/*

      1
   2     3
 4         5 


*/




func main() {
    //[1,2,3,4,null,null,5]

}

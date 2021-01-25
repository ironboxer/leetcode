/*

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.


Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?



Constraints:

The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

*/


package main


import "fmt"


type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}


func kthSmallest(root *TreeNode, k int) int {
    var res int = 0
    var f func(root *TreeNode)
    f = func(root *TreeNode) {
        if root != nil {
            f(root.Left)
            k--
            if k == 0 {
                res = root.Val
                return
            }
            f(root.Right)
        }
    }
    f(root)
    return res
}

func main() {

/*
    3
   / \
  1   4
   \
    2
*/
    var root *TreeNode = nil
    root = &TreeNode{3, nil, nil}
    root.Left = &TreeNode{1, nil, nil} 
    root.Right = &TreeNode{4, nil, nil}
    root.Left.Right = &TreeNode{2, nil, nil}
    r := kthSmallest(root, 3)
    fmt.Println(r)
}


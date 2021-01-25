/*

https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

*/

package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxPathSum(root *TreeNode) int {
	max := func(nums ...int) int {
		val := nums[0]
		for i := 1; i < len(nums); i++ {
			if nums[i] > val {
				val = nums[i]
			}
		}
		return val
	}
	isNull := func(root *TreeNode) bool {
		return root == nil
	}
	isLeaf := func(root *TreeNode) bool {
		return root != nil && root.Left == nil && root.Right == nil
	}
	maxVal := int(-(2 << 30))
	var f func(root *TreeNode) int
	f = func(root *TreeNode) int {
		if isNull(root) {
			return 0
		}
		if isLeaf(root) {
			maxVal = max(maxVal, root.Val)
			return root.Val
		}
		v, l, r := root.Val, f(root.Left), f(root.Right)
		maxVal = max(maxVal, v, l+v, r+v, l+r+v)
		// 这个题有点怪 不允许子树同时存在左右的和
		// 非常奇怪的一个点
		return max(v, l+v, r+v)
	}
	f(root)
	return maxVal
}

func main() {
	// [-10,9,20,null,null,15,7]
	root := &TreeNode{-10, nil, nil}
	root.Left = &TreeNode{9, nil, nil}
	root.Right = &TreeNode{20, nil, nil}
	root.Right.Left = &TreeNode{15, nil, nil}
	root.Right.Right = &TreeNode{7, nil, nil}

	fmt.Println(maxPathSum(root))

	root = &TreeNode{1, nil, nil}
	root.Left = &TreeNode{2, nil, nil}
	root.Right = &TreeNode{3, nil, nil}
	fmt.Println(maxPathSum(root))

	root = &TreeNode{0, nil, nil}
	fmt.Println(maxPathSum(root))

	root = &TreeNode{-2, nil, nil}
	root.Left = &TreeNode{-1, nil, nil}
	fmt.Println(maxPathSum(root))

	// [5,4,8,11,null,13,4,7,2,null,null,null,1]
	root = &TreeNode{5, nil, nil}
	root.Left = &TreeNode{4, nil, nil}
	root.Right = &TreeNode{8, nil, nil}
	root.Left.Left = &TreeNode{11, nil, nil}
	root.Right.Left = &TreeNode{13, nil, nil}
	root.Right.Right = &TreeNode{4, nil, nil}
	root.Left.Left.Left = &TreeNode{7, nil, nil}
	root.Left.Left.Right = &TreeNode{2, nil, nil}
	root.Right.Right.Right = &TreeNode{1, nil, nil}
	fmt.Println(maxPathSum(root))
}

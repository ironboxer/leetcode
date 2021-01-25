/*


https://leetcode.com/problems/binary-search-tree-iterator/

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.



Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false


Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

*/

package main

import "fmt"


type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}


type BSTIterator struct {
    Nodes []*TreeNode
    Pos int
}


func visit(root *TreeNode, stack *[]*TreeNode) {
    if root != nil {
        visit(root.Left, stack)
        *stack = append(*stack, root)
        visit(root.Right, stack)
    }
}


func Constructor(root *TreeNode) BSTIterator {
    nodes := make([]*TreeNode, 0)
    visit(root, &nodes)
    fmt.Println(nodes)
    obj := BSTIterator {
        Nodes: nodes, 
        Pos: 0,
    } 
    return obj
}


/** @return the next smallest number */
func (this *BSTIterator) Next() int {
    node := this.Nodes[this.Pos]
    this.Pos++
    return node.Val
}


/** @return whether we have a next smallest number */
func (this *BSTIterator) HasNext() bool {
    return this.Pos < len(this.Nodes) 
}



func main() {
    root := &TreeNode{7, nil, nil}
    root.Left = &TreeNode{3, nil, nil}
    root.Right = &TreeNode{15, nil, nil}
    root.Right.Left = &TreeNode{9, nil, nil}
    root.Right.Right = &TreeNode{20, nil, nil} 
    obj := Constructor(root)
    for obj.HasNext() {
        fmt.Println(obj.Next())
    }
}


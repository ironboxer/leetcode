/*

https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Example 1:



Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100

*/


package main


import "fmt"


type Node struct {
    Val int
    Left *Node
    Right *Node
    Next *Node
}


type LevelNode struct {
    TreeNode *Node 
    Level int
}


func connect(root *Node) *Node {
    if root == nil {
        return root
    }
    queue := make([]*LevelNode, 0)
    queue = append(queue, &LevelNode{TreeNode: root, Level: 0})
    var last *LevelNode = nil
    for len(queue) > 0 {
        node := queue[0]
        queue = queue[1:]
        if last != nil && last.Level == node.Level {
            last.TreeNode.Next = node.TreeNode
        }
        last = node
        if node.TreeNode.Left != nil {
            queue = append(queue, &LevelNode{TreeNode: node.TreeNode.Left, Level: node.Level + 1})
        }
        if node.TreeNode.Right != nil {
            queue = append(queue, &LevelNode{TreeNode: node.TreeNode.Right, Level: node.Level + 1})
        }
    }
    return root
}


// 考察的还是二叉树的遍历方式
// DFS 不行的 就用BFS


func main() {
    // [1,2,3,4,5,null,7]
    root := &Node{1, nil, nil, nil}
    root.Left = &Node{2, nil, nil, nil}
    root.Right = &Node{3, nil, nil, nil}
    root.Left.Left = &Node{4, nil, nil, nil}
    root.Left.Right = &Node{5, nil, nil, nil}
    root.Right.Right = &Node{7, nil, nil, nil}

    root = connect(root)
    fmt.Println(root)
}

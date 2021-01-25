/*

https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


# preorder: 1 2 3 4 5
# inorder : 2 1 4 3 5

*/


package main


import "fmt"
import "strconv"
import "strings"


func str2int(s string) int {
    v, err := strconv.Atoi(s)
    if err != nil {
        return -1
    }
    return v
}


func int2str(n int) string {
    return strconv.Itoa(n)
}


type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}


type Codec struct {

}


func Constructor() Codec {
    obj := Codec{}
    return obj
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
    var f func(root *TreeNode) string
    f = func(root *TreeNode) string {
        if root == nil {
            return "+"
        }
        val := int2str(root.Val)
        left := f(root.Left)
        right := f(root.Right)
        return val + "," + left + "," + right
    }
    return f(root)
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
    // 这个构建的过程需要好好想一下
    tokens := strings.Split(data, ",")
    i, N := -1, len(tokens)
    var f func() *TreeNode 
    f = func() *TreeNode {
        i++
        if i == N {
            return nil
        }
        if tokens[i] == "+" {
            return nil
        }
        root := &TreeNode{str2int(tokens[i]), nil, nil}
        root.Left = f()
        root.Right = f()
        return root
    }
    return f()
}


func visit(root *TreeNode) {
    if root != nil {
        visit(root.Left)
        fmt.Println(root.Val)
        visit(root.Right)
    }
}


func main() {
    var root *TreeNode = nil
    root = &TreeNode{1, nil, nil}
    root.Left = &TreeNode{2, nil, nil}
    root.Right = &TreeNode{3, nil, nil}
    root.Right.Left = &TreeNode{4, nil, nil}
    root.Right.Right = &TreeNode{5, nil, nil}
    
    codec := Constructor()
    data := codec.serialize(root)
    fmt.Println(data)
    newRoot := codec.deserialize(data)
    visit(newRoot)
}

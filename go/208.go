/*

https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

*/

package main


import "fmt"

type Node struct {
    Val byte
    End bool
    Children map[byte]*Node
}


type Trie struct {
    Root *Node
}


/** Initialize your data structure here. */
func Constructor() Trie {
    children := make(map[byte]*Node)
    root := &Node{'#', false, children}
    obj := Trie{Root: root}
    return obj
}


/** Inserts a word into the trie. */
func (this *Trie) Insert(word string) {
    node := this.Root
    for i := 0; i < len(word); i++ {
        c := word[i]
        subNode, ok := node.Children[c]
        if !ok {
            children := make(map[byte]*Node)
            subNode = &Node{c, false, children}
            node.Children[c] = subNode
        }
        node = subNode
    }
    node.End = true
}


/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
    node := this.Root
    for i := 0; i < len(word); i++ {
        c := word[i]
        subNode, ok := node.Children[c]
        if !ok {
            return false
        }
        node = subNode
    }
    return node.End
}


/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
    node := this.Root
    for i := 0; i < len(prefix); i++ {
        c := prefix[i]
        subNode, ok := node.Children[c]
        if !ok {
            return false
        }
        node = subNode
    }
    return true
}


func main() {
    trie := Constructor()
    trie.Insert("apple")
    fmt.Println(trie.Search("apple"))
    fmt.Println(trie.Search("app"))
    fmt.Println(trie.StartsWith("app"))
    trie.Insert("app")
    fmt.Println(trie.Search("app"))
}


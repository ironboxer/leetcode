/*

https://leetcode.com/problems/word-search-ii/

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]


Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.

*/


package main


import "fmt"


type TrieNode struct {
    Val byte
    End bool
    Children map[byte]*TrieNode
}


type Trie struct {
    Root *TrieNode
}


func (this *Trie) Add(word string) {
    node := this.Root
    for i := 0; i < len(word); i++ {
        w := word[i]
        subNode, ok := node.Children[w]
        if !ok {
            children := make(map[byte]*TrieNode, 0)
            subNode = &TrieNode{w, false, children}
            node.Children[w] = subNode
        }
        node = subNode
    }
    node.End = true
}


func Constructor() Trie {
    children := make(map[byte]*TrieNode, 0)
    root := &TrieNode{'#', false, children}
    obj := Trie{root}
    return obj
}


func findWords(board [][]byte, words []string) []string {
    m, n := len(board), len(board[0])
    trie := Constructor()
    for _, word := range words {
        trie.Add(word)
    }
    res := make([]string, 0)
    var f func(i, j int, s string, node *TrieNode)
    f = func(i, j int, s string, node *TrieNode) {
        if node.End {
            res = append(res, s)
            node.End = false
        }
        if i < 0 || j < 0 || i >= m || j >= n {
            return
        }
        x := board[i][j]
        subNode, ok := node.Children[x]
        if !ok {
            return
        }
        node = subNode
        ns := s + string([]byte{x})
        board[i][j] = '#'
        f(i+1, j, ns, node)
        f(i-1, j, ns, node)
        f(i, j+1, ns, node)
        f(i, j-1, ns, node)
        board[i][j] = x
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            f(i, j, "", trie.Root)
        }
    }
    return res
}


// slow but work

/*
func findWords(board [][]byte, words []string) []string {
    m, n := len(board), len(board[0])
    var f func(i, j int, word string) bool
    f = func(i, j int, word string) bool {
        if len(word) == 0 {
            return true
        }
        if i < 0 || j < 0 || i >= m  || j >= n {
            return false
        }
        if board[i][j] != word[0] {
            return false
        }
        tmp := board[i][j]
        board[i][j] = '#'
        r := f(i+1, j, word[1:]) || f(i-1, j, word[1:]) || f(i, j+1, word[1:]) || f(i, j-1, word[1:])
        board[i][j] = tmp
        return r
    }
    g := func(word string) bool {
        for i := 0; i < m; i++ {
            for j := 0; j < n; j++ {
                if f(i, j, word) {
                    return true
                }
            }
        } 
        return false
    }
    res := make([]string, 0)
    for _, word := range words {
        i:f g(word) {
            res = append(res, word)
        }
    }
    return res
}
*/


func main() {
    board := [][]byte {
        {'o', 'a', 'a', 'n'},
        {'e', 't', 'a', 'e'},
        {'i', 'h', 'k', 'r'},
        {'i', 'f', 'l', 'v'},
    }
    words := []string{"oath","pea","eat","rain"}
    res := findWords(board, words)
    fmt.Println(res) 

    board = [][]byte {
        {'a', 'a'},
    }
    words = []string{"aaa"}
    res = findWords(board, words)
    fmt.Println(res)
}

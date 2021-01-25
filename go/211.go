/*

https://leetcode.com/problems/add-and-search-word-data-structure-design/

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.

*/

package main


import "fmt"

type WordDictionary struct {
    Bucket map[int][]string
}


/** Initialize your data structure here. */
func Constructor() WordDictionary {
    bucket := make(map[int][]string)
    obj := WordDictionary{Bucket: bucket}
    return obj
}


/** Adds a word into the data structure. */
func (this *WordDictionary) AddWord(word string)  {
    list, ok := this.Bucket[len(word)] 
    if !ok {
        list = make([]string, 0)
    }
    this.Bucket[len(word)] = append(list, word)
}



/** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
func (this *WordDictionary) Search(word string) bool {
    list, ok := this.Bucket[len(word)]
    if ok {
        for i := 0; i < len(list); i++ {
            w := list[i]            
            j := 0
            for ;j < len(w); j++ {
                if !(word[j] == w[j] || word[j] == '.') {
                    break
                }
            }
            if j == len(w) {
                return true
            }
        }
    }
    return false
}


func main() {
    obj := Constructor()
    obj.AddWord("bad")
    obj.AddWord("dad")
    obj.AddWord("mad")
    fmt.Println(obj.Search("pad"))
    fmt.Println(obj.Search("bad"))
    fmt.Println(obj.Search(".ad"))
    fmt.Println(obj.Search("b.."))
}

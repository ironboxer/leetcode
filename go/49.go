/*

https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.

*/


package main


import "fmt"

import "sort"
import "strings"


func groupAnagrams(strs []string) [][]string {
    dict := make(map[string][]string)    
    for _, e := range strs {
        s := strings.Split(e, "")
        sort.Strings(s)
        t := strings.Join(s, "")
        items, ok := dict[t]
        if ok {
            dict[t] = append(items, e)
        } else {
            dict[t] = make([]string, 0)
            dict[t] = append(dict[t], e)
        }
    }
    res := make([][]string, 0)
    for _, items := range dict {
        res = append(res, items)
    }
    return res
}


func main() {
    strs := []string{"eat","tea","tan","ate","nat","bat"}
    fmt.Println(groupAnagrams(strs))
}

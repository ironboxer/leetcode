/*

https://leetcode.com/problems/letter-combinations-of-a-phone-number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].  Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

*/


package main


import "fmt"
import "strings"


func letterCombinations(digits string) []string {
    if len(digits) == 0 {
        return []string{}
    }
    dict := map[string][]string {
        "2": []string{"a", "b", "c"},
        "3": []string{"d", "e", "f"},
        "4": []string{"g", "h", "i"},
        "5": []string{"j", "k", "l"},
        "6": []string{"m", "n", "o"},
        "7": []string{"p", "q", "r", "s"},
        "8": []string{"t", "u", "v"},
        "9": []string{"w", "x", "y", "z"},
    }
    buf := make([][]string, len(digits))
    for i, d := range digits {
        buf[i] = dict[string(d)]
    }
    res := make([][]string, 0)
    res = append(res, []string{})
    for _, items := range buf {
        tmp := make([][]string, 0)
        for _, j := range items {
            for _, i := range res {
                p := make([]string, len(i) + 1)
                copy(p, i)
                p[len(i)] = j
                tmp = append(tmp, p)
                //fmt.Println(tmp)
            }
        }
        res = tmp
    } 
    //fmt.Println(res)
    str := make([]string, len(res))
    for i, e := range res {
        str[i] = strings.Join(e, "")
    }
    return str
}

// Python中的itertools中的permutation

func main() {
    s := "23"
    fmt.Println(letterCombinations(s))

    s = ""
    fmt.Println(letterCombinations(s))
}



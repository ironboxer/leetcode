/*

https://leetcode.com/problems/excel-sheet-column-title/

https://leetcode.com/problems/excel-sheet-column-title/

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

*/

package main


import "fmt"


func convertToTitle(n int) string {
    dict := make(map[int]string)
    for i := 0; i < 26; i++ {
        dict[i] = string(byte(i) + 'A')
    }
    
    res := ""
    for n != 0 {
        n--
        res = dict[(n + 26 ) % 26] + res
        n = n / 26
    }
    return res
}


//费了九牛二虎之力


func main() {
    /*
    for i := 1; i < 1000; i++ {
        fmt.Println(i, convertToTitle(i))
    }
    */
    fmt.Println(1, convertToTitle(1))
    fmt.Println(28, convertToTitle(28))
    fmt.Println(701, convertToTitle(701))
}

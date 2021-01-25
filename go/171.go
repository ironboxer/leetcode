/*

https://leetcode.com/problems/excel-sheet-column-number/

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701


Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".

*/


package main


import "fmt"


func titleToNumber(s string) int {
    r := 0
    for _, c := range s {
        n := int(c - 'A') + 1
        r = r * 26 + n
    }
    return r
}


func main() {
    fmt.Println("A", titleToNumber("A"))
    fmt.Println("AB", titleToNumber("AB"))
    fmt.Println("ZY", titleToNumber("ZY"))
}

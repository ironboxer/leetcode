/*


https://leetcode.com/problems/roman-to-integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

*/


package main

import "strings"


type Node struct {
    Key string
    Val int
}


func romanToInt(s string) int {
    table := []Node {
        Node{Key: "M", Val: 1000},
        Node{Key: "CM", Val: 900},
        Node{Key: "D", Val: 500},
        Node{Key: "CD", Val: 400},
        Node{Key: "C", Val: 100},
        Node{Key: "XC", Val: 90},
        Node{Key: "L", Val: 50},
        Node{Key: "XL", Val: 40},
        Node{Key: "X", Val: 10},
        Node{Key: "IX", Val: 9},
        Node{Key: "V", Val: 5},
        Node{Key: "IV", Val: 4},
        Node{Key: "I", Val: 1},
    }    

    r := 0
    for ;len(s) > 0; {
        for _, node := range table {
            if strings.HasPrefix(s, node.Key) {
                s = s[len(node.Key):]
                r += node.Val
                break
            }
        }
    }
    return r
}


func main() {
    s := "I"
    println(s, romanToInt(s))

    s = "III"
    println(s, romanToInt(s))

    s = "IV"
    println(s, romanToInt(s))

    s = "IX"
    println(s, romanToInt(s))

    s = "LVIII"
    println(s, romanToInt(s))

    s = "MCMXCIV"
    println(s, romanToInt(s))
}

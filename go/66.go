/*

https://leetcode.com/problems/plus-one/

Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9

*/
package main


import "fmt"


func plusOne(digits []int) []int {
    t := 1
    for i := len(digits) - 1; i >= 0; i-- {
        r := digits[i] + t
        digits[i] = r % 10
        t = r / 10
    }
    if t == 0 {
        return digits
    }
    buf := make([]int, len(digits) + 1)
    copy(buf[1:], digits)
    buf[0] = t
    return buf
}


func main() {
    digits := []int{1, 2, 3}
    fmt.Println(plusOne(digits))
    
    digits = []int{9}
    fmt.Println(plusOne(digits))
}

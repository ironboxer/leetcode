/*

https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

*/

package main


import "fmt"
import "strings"


func isPalindrome(s string) bool {
    s = strings.ToLower(s) 
    left, right := 0, len(s) - 1
    for left < right {
        if !(97 <= s[left] && s[left] <= 122 || 48 <= s[left] && s[left] <= 57) {
            left++
        } else if !(97 <= s[right] && s[right] <= 122 || 48 <= s[right] && s[right] <= 57) {
            right--
        } else if s[left] != s[right] {
            return false
        } else {
            left++
            right--
        }    
    }
    return true
}


func main() {
    s := "A man, a plan, a canal: Panama"
    fmt.Println(isPalindrome(s))

    s = "ABA"
    fmt.Println(isPalindrome(s))

    s = "0P"
    fmt.Println(isPalindrome(s))
}


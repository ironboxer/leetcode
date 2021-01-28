/*
https://leetcode-cn.com/problems/palindrome-partitioning-ii/


132. 分割回文串 II
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。


说明下面的方案有问题 不应该使用

需要其他的方案
*/

package main

import "fmt"

var words = make(map[string]bool)
var dict = make(map[string]int)


func min(a, b int) int  {
    if a <= b {
        return a
    }
    return b
}


func check(s string) bool {
    if v, ok := words[s]; ok {
        return v
    }
    l, r := 0, len(s) - 1
    for l < r {
        if s[l] != s[r] {
            words[s] = false
            return false
        }
        l++
        r--
    }
    words[s] = true
    return true
}


func minCut(s string) int {
    if v, ok := dict[s]; ok {
        return v
    }
    if check(s) {
        return 0
    }
    var res = len(s) - 1
    for i := 1; i < len(s); i++ {
        l, r := minCut(s[:i]), minCut(s[i:])
        res = min(res, l + r + 1)
    }
    dict[s] = res
    return res
}


func main() {
    //var s = "aab"
    //var e = 1
    //var s = "eegiicgaeadbcfacfhifdgj"
    //var e = 18
    //var s = "eegiicgaeadbcfacfhifdbiehbgejcaeggcgbahfcajfhjjdgj"
    //var e = 42
    var s = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
    var e = 452
    var r = minCut(s)
    fmt.Println(r, r == e)
}



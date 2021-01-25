/*

https://leetcode.com/problems/h-index/

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.

*/

package main


import "fmt"


func hIndex(citations []int) int {
    n := len(citations)
    buf := make([]int, n + 1)
    for _, e := range citations {
        if e >= n {
            buf[n]++
        } else {
            buf[e]++
        }
    }
    fmt.Println(buf)
    res := 0
    for i := n; i >= 0; i-- {
        res = res + buf[i]
        if res >= i {
            return i
        }
    }
    return 0
}


func main() {
    citations := []int{3,0,6,1,5}
    fmt.Println(hIndex(citations))

    citations = []int{0}
    fmt.Println(hIndex(citations))

    citations = []int{1}
    fmt.Println(hIndex(citations))
}


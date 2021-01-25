/*

https://leetcode.com/problems/h-index-ii/

Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had
             received 0, 1, 3, 5, 6 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?

*/


package main


import "fmt"


/*
func hIndex(citations []int) int {
    for len(citations) > 0 && citations[0] < len(citations) {
        citations = citations[1:]
    }
    return len(citations)
}
*/


// 在黑暗中苦苦摸索
func hIndex(citations []int) int {
    N := len(citations)
    left, right := 0, N - 1
    for left <= right {
        mid := left + (right - left) / 2
        if citations[mid] >= N - mid {
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    return N - left
}


func main() {
    citations := []int{0, 1, 3, 5, 6}
    fmt.Println(hIndex(citations))

    citations = []int{0}
    fmt.Println(hIndex(citations))

    citations = []int{1}
    fmt.Println(hIndex(citations))

    citations = []int{0, 1}
    fmt.Println(hIndex(citations))

    citations = []int{11, 15}
    fmt.Println(hIndex(citations))
    
    citations = []int{1,1,2,3,4,5,7}
    fmt.Println(hIndex(citations))
}

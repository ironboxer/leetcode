/*

https://leetcode.com/problems/ugly-number-ii/

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.

*/


package main


import "fmt"

/*
2 * 1, 2 * 2, 2 * 3
3 * 1, 3 * 2, 3 * 3
5 * 1, 5 * 2, 5 * 3

*/



func min(nums ...int) int {
    a := nums[0]
    for i := 1; i < len(nums); i++ {
        if nums[i] < a {
            a = nums[i]
        }
    }
    return a
}


/*
func nthUglyNumber(n int) int {
    buf := make([]int, 0)
    buf = append(buf, 1)
    a, b, c := 0, 0, 0
    for len(buf) < n {
        for buf[a] * 2 <= buf[len(buf)-1] {
            a++
        }
        for buf[b] * 3 <= buf[len(buf)-1] {
            b++
        }
        for buf[c] * 5 <= buf[len(buf)-1] {
            c++
        }
        buf = append(buf, min(buf[a] * 2, buf[b] * 3, buf[c] * 5))
    }
    return buf[n-1]
}
*/

func nthUglyNumber(n int) int {
    buf := make([]int, n)
    j := 0
    buf[j] = 1
    a, b, c := 0, 0, 0
    for j + 1 < n {
        for buf[a] * 2 <= buf[j] {
            a++
        }
        for buf[b] * 3 <= buf[j] {
            b++
        }
        for buf[c] * 5 <= buf[j] {
            c++
        }
        buf[j+1] = min(buf[a] * 2, buf[b] * 3, buf[c] * 5)
        j++
    }
    return buf[n-1]
}


func main() {
    fmt.Println(nthUglyNumber(1690))
}


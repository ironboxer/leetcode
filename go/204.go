/*

https://leetcode.com/problems/count-primes/

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

*/

package main


import "fmt"


func countTrue(nums []bool) int {
    res := 0
    for i := 0; i < len(nums); i++ {
        if nums[i] {
            res++
        }
    }
    return res
}


// less than n
func countPrimes(n int) int {
    if n < 2 {
        return 0
    }
    prime := make([]bool, n)
    for i := 0; i < n; i++ {
        prime[i] = true
    }
    prime[0] = false
    prime[1] = false
    for i := 2; i * 2 < n; i++ {
        for j := 2; i * j < n; j++ {
            prime[i * j] = false
        }
    }
    return countTrue(prime)
}


func main() {
    fmt.Println(countPrimes(50))
}


/*

https://leetcode.com/problems/permutation-sequence/

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

https://leetcode.com/problems/permutation-sequence/discuss/22512/Share-my-Python-solution-with-detailed-explanation

*/


package main


import "fmt"

import "strconv"


func factorial(n int) int {
    r := 1
    for n > 0 {
        r = r * n
        n--
    }
    return r
}


func divmod(m int, n int) (int, int) {
    a := m / n
    b := m % n
    return a, b
}


func getPermutation(n int, k int) string {
    nums := make([]string, n)
    for i := 0; i < n; i++ {
        nums[i] = strconv.Itoa(i+1)
    }
    res := ""
    k--
    for n > 0 {
        n--
        i, j := divmod(k, factorial(n))
        res = res + nums[i]
        nums = append(nums[:i], nums[i+1:]...)
        k = j
    }
    return res
}


// 这是一种特定的算法 对于这种特定的算法 只能理解+记忆


func main() {
    fmt.Println(getPermutation(3, 3))
    fmt.Println(getPermutation(3, 5))
    fmt.Println(getPermutation(4, 9))
}


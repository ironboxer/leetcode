/*

https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.

*/


package main


import "fmt"


func topKFrequent(nums []int, k int) []int {
    dict := make(map[int]int)
    for _, e := range nums {
        v, ok := dict[e]
        if !ok {
            v = 0
        }
        dict[e] = v + 1
    }
    // something link bucket sort
    buckets := make([][]int, len(nums) + 1)
    for key, val := range dict {
        if len(buckets[val]) == 0 {
            buckets[val] = make([]int, 0)
        }
        buckets[val] = append(buckets[val], key)
    }
    res := make([]int, 0)
    for i := len(nums); i >= 0; i-- {
        list := buckets[i]
        for j := 0; j < len(list); j++ {
            res = append(res, list[j])
        }
        if len(res) >= k {
            break
        }
    }        
    return res[:k]
}


func main() {
    nums := []int{1,1,1,2,2,3}
    k := 2
    fmt.Println(topKFrequent(nums, k))

    nums = []int{1}
    k = 1
    fmt.Println(topKFrequent(nums, k))

}

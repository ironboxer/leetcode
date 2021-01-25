/*

https://leetcode.com/problems/random-pick-index/

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);

*/


package main


import "fmt"
import "math/rand"


type Solution struct {
    Buckets map[int][]int
}


func Constructor(nums []int) Solution {
    buckets := make(map[int][]int)
    for i, e := range nums {
        bucket, ok := buckets[e]
        if !ok {
            bucket = make([]int, 0)
        }
        bucket = append(bucket, i)
        buckets[e] = bucket
    }
    obj := Solution{buckets}
    return obj
}


func (this *Solution) Pick(target int) int {
    bucket, _ := this.Buckets[target]
    i := rand.Int()
    p := i % len(bucket)
    return bucket[p]
}


func main() {
    nums := []int{1,2,3,4,5,1,2,3,4,1,2,3,1,2,1}
    s := Constructor(nums)
    for i := 0; i < len(nums); i++ {
        fmt.Println(s.Pick(nums[i]))
    }
}

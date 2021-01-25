/*

https://leetcode.com/problems/range-sum-query-mutable/

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8


Constraints:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
0 <= i <= j <= nums.length - 1

// 用到了一种高级的数据结构 线段树
http://codeforces.com/blog/entry/18051


// golang中还是缺少一些高级的数据结构 需要我们自己的实现啊

*/

package main


import "fmt"


type NumArray struct {
    Nums []int
}


func Constructor(nums []int) NumArray {
    tmp := make([]int, len(nums)) 
    copy(tmp, nums)
    obj := NumArray{tmp}
    return obj
}


func (this *NumArray) Update(i int, val int)  {
    this.Nums[i] = val
}


func (this *NumArray) SumRange(i int, j int) int {
    s := 0
    for i <= j {
        s = s + this.Nums[i]
        i++
    }
    return s
}


func main() {
    obj := Constructor(nums);
}

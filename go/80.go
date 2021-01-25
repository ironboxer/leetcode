/*

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

*/


package main


import "fmt"


func removeDuplicates(nums []int) int {
    p := 0
    for i := 0; i < len(nums); i++ {
        if i == 0 {
            p++
        } else if nums[i] != nums[p-1] || p == 1 {
            nums[p] = nums[i]
            p++
        } else if p > 1 && nums[p-1] != nums[p-2] {
            nums[p] = nums[i]
            p++
        }
    }
    return p
}


func main() {
    nums := []int{1,1,1,2,2,3}
    k := removeDuplicates(nums)
    fmt.Println(nums[:k])

    nums = []int{0,0,1,1,1,1,2,3,3}
    k = removeDuplicates(nums)
    fmt.Println(nums[:k])
}


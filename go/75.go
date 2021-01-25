/*

https://leetcode.com/problems/sort-colors/

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?


Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.

*/


package main

import "fmt"


func sortColors(nums []int)  {
    if len(nums) == 0 {
        return
    }
    l, r := 0, len(nums) - 1
    for i := l; i <= r; {
        if nums[r] == 2 {
            r--
        } else if nums[l] == 0 {
            l++
            i++
        } else {
            if nums[i] == 2 {
                nums[i], nums[r] = nums[r], nums[i]
            } else if nums[i] == 0 {
                nums[i], nums[l] = nums[l], nums[i]
            } else {
                i++
            }
        }
    }
}


func main() {
    nums := []int{2,0,2,1,1,0}
    fmt.Println(nums)
    sortColors(nums)
    fmt.Println(nums)

    nums = []int{2, 0, 1}
    fmt.Println(nums)
    sortColors(nums)
    fmt.Println(nums)

}

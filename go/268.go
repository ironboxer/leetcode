/*

https://leetcode.com/problems/missing-number/

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

*/


package main


import "fmt"

/*

public int missingNumber(int[] nums) {

    int xor = 0, i = 0;
	for (i = 0; i < nums.length; i++) {
		xor = xor ^ i ^ nums[i];
	}

	return xor ^ i;
}

*/

// sum range 多摩简单
func missingNumber(nums []int) int {
    s, n := 0, len(nums)
    for i := 0; i < len(nums); i++ {
        // 如果 nums[i] == i 则 s = 0
        s = s ^ (i ^ nums[i])
    }
    // 如果 s == 0, s ^ n == n
    return s ^ n
}


func main() {
    nums := []int{3, 0, 1}
    fmt.Println(missingNumber(nums))

    nums = []int{9,6,4,2,3,5,7,0,1}
    fmt.Println(missingNumber(nums))
    
    nums = []int{1}
    fmt.Println(missingNumber(nums))
}

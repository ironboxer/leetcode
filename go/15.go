/*


https://leetcode.com/problems/3sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105


*/

package main

import "fmt"


/*
func bsearch(nums []int, left, right, target int) int {
    for ;left <= right; {
        mid := left + (right - left) / 2
        if nums[mid] < target {
            left = mid + 1
        } else if nums[mid] > target {
            right = mid - 1
        } else {
            return mid
        }
    }
    return right
}


func threeSum(nums []int) [][]int {
    sort.Ints(nums)
    left, right := 0, len(nums) - 1
    res := make([][]int, 0)
    for ;left + 1 < right; {
        t := 0 - nums[left] - nums[right]
        if t < nums[left] || t > nums[right] {
            break
        }
        i := bsearch(nums, left+1, right-1, t)
        if i > left && i < right && nums[i] == t {
            res = append(res, []int{nums[left], nums[i], nums[right]})
            left++
            right--
        } else {
            if nums[i] < t {
                left++
            } else {
                right--
            }
        }
    } 
    return res
}
*/


// 二分查找在找不到的情况下无法指导下一步应该具体的走向
// 所以不是一个号的思路



func threeSum(nums []int) [][]int {
    dict := make(map[int]int)
    for _, e := range nums {
        i, ok := dict[e]
        if !ok {
            i = 0
        }
        dict[e] = i + 1
    }
    dup := make(map[[3]int]bool)
    res := make([][]int, 0) 
    for i, v1 := range dict {
        for j, v2 := range dict {
            if i == j && v2 < 2 {
                continue
            }
            t := 0 - i - j
            v3, ok := dict[t]
            if ok {
                if t == i && v1 < 2 {
                    continue
                }
                if t == j && v2 < 2 {
                    continue
                }
                if t == i && t == j && v3 < 3 {
                    continue
                }
                arr := [3]int{i, j, t}
                if arr[0] > arr[1] {
                    arr[0], arr[1] = arr[1], arr[0]
                }
                if arr[1] > arr[2] {
                    arr[1], arr[2] = arr[2], arr[1]
                }
                if arr[0] > arr[1] {
                    arr[0], arr[1] = arr[1], arr[0]
                }
                _, ext := dup[arr]
                if ext {
                    continue
                }
                dup[arr] = true
                res = append(res, arr[:])
            }
        }
    } 
    return res
}

// 字典的作用在于将时间复杂度从O(n^3)减小到O(n^2)


func main()  {
    nums := []int{-1,0,1,2,-1,-4}
    res := threeSum(nums)
    fmt.Println(nums, res)

    nums = []int{1,2,-2,-1}
    res = threeSum(nums)
    fmt.Println(nums, res)

    nums = []int{-2,0,1,1,2}
    res = threeSum(nums)
    fmt.Println(nums, res)

    nums = []int{1,-1,-1,0}
    res = threeSum(nums)
    fmt.Println(nums, res)

    nums = []int{-2,0,0,2,2}
    res = threeSum(nums)
    fmt.Println(nums, res)
}





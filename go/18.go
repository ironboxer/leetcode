/*

https://leetcode.com/problems/4sum/

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

*/

package main

import "sort"
import "fmt"

/*
func fourSum(nums []int, target int) [][]int {
    dict := make(map[int]int)
    for _, e := range nums {
        v, ok := dict[e]
        if !ok {
            v = 0
        }
        dict[e] = v + 1
    }
    dup := make(map[[4]int]bool)
    res := make([][]int, 0)
    for i, _ := range dict {
        for j, v2 := range dict {
            if i == j && v2 < 2 {
                continue
            }
            for k, v3 := range dict {
                if (i == k || j == k) && v3 < 2 {
                    continue
                }
                if (i == k && j == k) && v3 < 3 {
                    continue
                }
                t := target - i - j - k
                v4, ok := dict[t]
                if ok {
                    if (i == t || j == t || k == t) && v4 < 2 {
                        continue
                    }
                    if (i == t && j == t || i == t && k == t || j == t && k == t) && v4 < 3 {
                        continue
                    }
                    if (i == t && j == t && k == t) && v4 < 4 {
                        continue
                    }
                    tmp := [4]int{i, j, k, t}
                    sort.Ints(tmp[:])
                    _, ext := dup[tmp]
                    if ext {
                        continue
                    }
                    dup[tmp] = true
                    res = append(res, tmp[:])
                }
            }
        }
    }
    return res
}
*/


func findNsum(nums []int, target int, N int, result []int, results [][]int) [][]int {
	if len(nums) < N || N < 2 {
		return results
	}
	if N == 2 {
		l, r := 0, len(nums) - 1
        for ;l < r; {
            println(l, r, nums[l], nums[r], target)
			if nums[l] + nums[r] == target {
                buf := make([]int, len(result) + 2)
                copy(buf, result)
                buf[len(result)] = nums[l]
                buf[len(result)+1] = nums[r]
				results = append(results, buf)
				l++
				r--
				for ;l < r && nums[l] == nums[l-1]; {
					l++
				}
				for ;l < r && nums[r] == nums[r+1]; {
					r--
				}
			} else if nums[l] + nums[r] < target {
				l++
			} else {
				r--
			}
		}
	} else {
		for i := 0; i < len(nums) - N + 1; i++ {
			if target < nums[i] * N || target > nums[len(nums)-1] * N {
				break
			}
			if i == 0 || i > 0 && nums[i-1] != nums[i] {
                buf := make([]int, len(result) + 1)
                copy(buf, result)
                buf[len(result)] = nums[i]
				results = findNsum(nums[i+1:], target-nums[i], N-1, buf, results)
			}
		}
	}
    return results
}


// golang 的slice append是如此的男用


func fourSum(nums []int, target int) [][]int {
	sort.Ints(nums)
	results := make([][]int, 0)
	buf := make([]int, 0)
	return findNsum(nums, target, 4, buf, results)
}


// 字典的存在使得时间复杂度从O(n^4)降低到O(n^3)


func main() {
	nums := []int{1, 0, -1, 0, -2, 2}
	target := 0
	fmt.Println(nums, fourSum(nums, target))
}


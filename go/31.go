/*

https://leetcode.com/problems/next-permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

https://leetcode.com/problems/next-permutation/discuss/13867/C%2B%2B-from-Wikipedia

1. Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
2. Find the largest index l > k such that nums[k] < nums[l].
3. Swap nums[k] and nums[l].
4. Reverse the sub-array nums[k + 1:].

*/

package main


import "fmt"


func nextPermutation(nums []int)  {
    if len(nums) < 2 {
        return
    }
    k := -1
    for i := len(nums) - 2; i >= 0; i-- {
        if nums[i] < nums[i+1] {
            k = i
            break
        }
    }
    if k == -1 {
        l, r := 0, len(nums) - 1
        for l < r {
            nums[l], nums[r]  = nums[r], nums[l]
            l++
            r--
        }
    } else {
        l := len(nums) - 1
        for l > k {
            if nums[k] < nums[l] {
                break
            }
            l--
        }
        nums[k], nums[l] = nums[l], nums[k]
        left, right := k + 1, len(nums) - 1
        for left < right {
            nums[left], nums[right] = nums[right], nums[left]
            left++
            right--
        }
    }
}


func main() {
    nums := []int{1,2,3}    
    fmt.Println(nums)    
    nextPermutation(nums)
    fmt.Println(nums)
    
    nums = []int{3,2,1}
    fmt.Println(nums)    
    nextPermutation(nums)
    fmt.Println(nums)

    nums = []int{3,1,2}
    fmt.Println(nums)    
    nextPermutation(nums)
    fmt.Println(nums)

    nums = []int{1,3,2}
    fmt.Println(nums)
    nextPermutation(nums)
    fmt.Println(nums)

    nums = []int{2,3,1}
    fmt.Println(nums)
    nextPermutation(nums)
    fmt.Println(nums)

}


/*

https://leetcode.com/problems/shuffle-an-array/

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

*/

package main


import "fmt"
import "math/rand"
import "time"


type Solution struct {
    Array []int
}


func Constructor(nums []int) Solution {
    obj := Solution{nums}
    return obj
}


/** Resets the array to its original configuration and return it. */
func (this *Solution) Reset() []int {
    return this.Array 
}


/** Returns a random shuffling of the array. */
func (this *Solution) Shuffle() []int {
    buf := make([]int, len(this.Array))
    copy(buf, this.Array)
    rand.Seed(time.Now().UnixNano()) 
    rand.Shuffle(len(buf), func(i, j int) {buf[i], buf[j] = buf[j], buf[i]})
    return buf
}


func main() {
    nums := []int{3,2, 1}    
    s := Constructor(nums)
    fmt.Println(s.Reset())
    fmt.Println(s.Shuffle())
    fmt.Println(s.Shuffle())
    fmt.Println(s.Reset())
}

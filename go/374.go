/*

https://leetcode.com/problems/guess-number-higher-or-lower/


We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6

*/

package main


import "fmt"


/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * func guess(num int) int;
 */


 func guess(num int) int {
     if num < 6 {
         return -1
     }
     if num > 6 {
         return 1
     }
     return 0
 }


func guessNumber(n int) int {
    low, high := 1, n
    for low <= high {
        mid := low + (high - low) / 2
        v := guess(mid)
        if v == 1 {
            low = mid + 1
        } else if v == -1 {
            high = mid - 1
        } else {
            return mid
        }
    }
    return 0
}



func main() {
    fmt.Println(guessNumber(10))
}

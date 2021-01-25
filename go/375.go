/*

https://leetcode.com/problems/guess-number-higher-or-lower-ii/


We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.



Constraints:

1 <= n <= 200
*/

package main

import "fmt"

func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a <= b {
		return a
	}
	return b
}

// 你能读懂什么意思吗?
func getMoneyAmount(n int) int {
	dict := make([][]int, n+1)
	for i := 0; i < n+1; i++ {
		dict[i] = make([]int, n+1)
	}
	var f func(s, e int) int
	f = func(s, e int) int {
		if s >= e {
			return 0
		}
		if dict[s][e] != 0 {
			return dict[s][e]
		}
		res := int((1 << 31) - 1)
		for x := s; x <= e; x++ {
			tmp := x + max(f(s, x-1), f(x+1, e))
			res = min(res, tmp)
		}
		dict[s][e] = res
		return res
	}
	return f(1, n)
}

func main() {
	fmt.Println(getMoneyAmount(10))
}

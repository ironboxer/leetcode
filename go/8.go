/*
https://leetcode.com/problems/string-to-integer-atoi/

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

*/

package main

import "strings"

func myAtoi(str string) int {
	s := strings.Trim(str, " ")
	if len(s) == 0 {
		return 0
	}
	if s[0] != '+' || s[0] != '-' {
		if s[0] < 48 && s[0] > 57 {
			return 0
		}
	}
	sign := 1
	if s[0] == '-' {
		sign = -1
		s = s[1:]
	} else if s[0] == '+' {
		s = s[1:]
	}
	var res uint64 = 0
	var resL uint64 = 0
	for i := 0; i < len(s); i++ {
		c := s[i]
		if c < 48 || c > 57 {
			break
		}
		res = res*10 + uint64(c-'0')
		if res < resL {
			res = resL
			break
		}
		// 超过uint64的范围
		resL = res
	}

	var maxInt uint64 = 1 << 31
	if sign == -1 && res > maxInt {
		return -(1 << 31)
	}
	if sign == 1 && res > maxInt-1 {
		return (1 << 31) - 1
	}
	return sign * int(res)
}

func main() {
	x := "-91283472332"
	println(x, myAtoi(x))

	x = "42"
	println(x, myAtoi(x))

	x = "   -42"
	println(x, myAtoi(x))

	x = "4193 with words"
	println(x, myAtoi(x))

	x = "words and 987"
	println(x, myAtoi(x))

	x = "+-2"
	println(x, myAtoi(x))

	x = "-   234"
	println(x, myAtoi(x))

	x = "18446744073709551617"
	println(x, myAtoi(x))

	x = "  0000000000012345678"
	println(x, myAtoi(x))

	x = "0-1"
	println(x, myAtoi(x))

	x = "0  123"
	println(x, myAtoi(x))

	x = "18446744073709551617"
	println(x, myAtoi(x))
}

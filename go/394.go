/*

https://leetcode.com/problems/decode-string/

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

好像每次都会走进死胡同
哪里有问题呢?
*/

package main

import "fmt"
import "strings"
import "strconv"

type Item interface{}
type Stack struct {
	items []Item
}

func (this *Stack) Push(item Item) {
	this.items = append(this.items, item)
}

func (this *Stack) Pop() Item {
	last := len(this.items) - 1
	val := this.items[last]
	this.items = this.items[:last]
	return val
}

func (this *Stack) Len() int {
	return len(this.items)
}

func (this *Stack) Empty() bool {
	return this.Len() == 0
}

func (this *Stack) Peek() Item {
	return this.items[len(this.items)-1]
}

func (this *Stack) Show() {
	fmt.Println(this.items)
}

// tokensize if the first step in compiler
func tokenize(s string) []string {
	tokens := make([]string, 0)
	n := ""
	str := ""
	for i := 0; i < len(s); i++ {
		c := s[i]
		if c >= 48 && c <= 57 {
			if len(str) > 0 {
				tokens = append(tokens, str)
				str = ""
			}
			n = n + string([]byte{c})
		} else if c == '[' {
			if len(n) > 0 {
				tokens = append(tokens, n)
				n = ""
			}
			tokens = append(tokens, string([]byte{c}))
		} else if c == ']' {
			if len(str) > 0 {
				tokens = append(tokens, str)
				str = ""
			}
			tokens = append(tokens, string([]byte{c}))
		} else {
			str = str + string([]byte{c})
		}
	}
	if len(str) > 0 {
		tokens = append(tokens, str)
	}
	return tokens
}

func isNumber(s string) bool {
	if _, err := strconv.Atoi(s); err != nil {
		return false
	}
	return true
}

func str2int(s string) int {
	v, _ := strconv.Atoi(s)
	return v
}

func repeat(s string, n int) string {
	sb := strings.Builder{}
	for n > 0 {
		sb.WriteString(s)
		n--
	}
	return sb.String()
}

// anything you didn't known?
func decodeString(s string) string {
	tokens := tokenize(s)
	fmt.Println(tokens)
	var res = ""
	var n = ""
	var stack = Stack{}
	// 3 [ a ] 2 [ b 4 [ F ] c ]
	for _, token := range tokens {
		if token == "[" {
			// push的是之前的元素
			stack.Push(res)
			stack.Push(n)
			res = ""
			n = ""
		} else if token == "]" {
			m := stack.Pop().(string)
			// pop的是之前的元素
			q := stack.Pop().(string)
			res = q + repeat(res, str2int(m))
		} else if isNumber(token) {
			n = token
		} else {
			res = res + token
		}
	}
	// 为什么这个思路正确的呢?
	return res
}

// 后面还需要好好想一下为甚磨
// 代码虽然很长 但是是自己的思路

func main() {

	s := "3[a]2[bc]"
	fmt.Println(decodeString(s))

	s = "3[a2[c]]"
	fmt.Println(decodeString(s))

	s = "2[abc]3[cd]ef"
	fmt.Println(decodeString(s))

	s = "abc3[cd]xyz"
	fmt.Println(decodeString(s))

	s = "3[a]2[b4[F]c]"
	// "aaabFFFFcbFFFFc"
	fmt.Println(decodeString(s))
}

/*

https://leetcode.com/problems/mini-parser/

Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

String is non-empty.
String does not contain white spaces.
String contains only digits 0-9, [, - ,, ].


Example 1:

Given s = "324",

You should return a NestedInteger object which contains a single integer 324.


Example 2:

Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.

*/

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * type NestedInteger struct {
 * }
 *
 * // Return true if this NestedInteger holds a single integer, rather than a nested list.
 * func (n NestedInteger) IsInteger() bool {}
 *
 * // Return the single integer that this NestedInteger holds, if it holds a single integer
 * // The result is undefined if this NestedInteger holds a nested list
 * // So before calling this method, you should have a check
 * func (n NestedInteger) GetInteger() int {}
 *
 * // Set this NestedInteger to hold a single integer.
 * func (n *NestedInteger) SetInteger(value int) {}
 *
 * // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 * func (n *NestedInteger) Add(elem NestedInteger) {}
 *
 * // Return the nested list that this NestedInteger holds, if it holds a nested list
 * // The list length is zero if this NestedInteger holds a single integer
 * // You can access NestedInteger's List element directly if you want to modify it
 * func (n NestedInteger) GetList() []*NestedInteger {}
 */

// s = "[123,[456,[789]]]"
/*
class Solution:
    def deserialize(self, s):
        stack, num, last = [], "", None
        for c in s:
            if c.isdigit() or c == "-": num += c
            elif c == "," and num:
                stack[-1].add(NestedInteger(int(num)))
                num = ""
            elif c == "[":
                elem = NestedInteger()
                if stack: stack[-1].add(elem)
                stack.append(elem)
            elif c == "]":
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""
                last = stack.pop()
        return last if last else NestedInteger(int(num))
*/

package main

import "strconv"

type Item interface{}

type Stack struct {
	Items []Item
}

func Constructor() Stack {
	items := make([]Item, 0)
	obj := Stack{items}
	return obj
}

func (this *Stack) Push(item Item) {
	this.Items = append(this.Items, item)
}

func (this *Stack) Pop() Item {
	last := len(this.Items) - 1
	item := this.Items[last]
	this.Items = this.Items[:last]
	return item
}

func (this *Stack) Len() int {
	return len(this.Items)
}

func (this *Stack) Empty() bool {
	return this.Len() == 0
}

func (this *Stack) Peek() Item {
	item := this.Items[this.Len()-1]
	return item
}

func isDigit(c byte) bool {
	return c >= 48 && c <= 57 || c == '-'
}

func str2int(s string) int {
	v, _ := strconv.Atoi(s)
	return v
}

func tokenize(s string) []string {
	num := ""
	stack := Constructor()
	for i := 0; i < len(s); i++ {
		c := s[i]
		if c == '[' {
			stack.Push(string([]byte{c}))
		} else if isDigit(c) {
			num = num + string([]byte{c})
		} else if c == ',' || c == ']' {
			if len(num) > 0 {
				stack.Push(str2int(num))
				num = ""
			}
			stack.Push(string([]byte{c}))
		}
	}
	if len(num) > 0 {
		stack.Push(str2int(num))
		num = ""
	}
	tokens := make([]string, stack.Len())
	for i := 0; i < stack.Len(); i++ {
		tokens[i] = stack.Items[i].(string)
	}
	return tokens
}

// 这里无法用go来实现 除非全部改成Interface
func decode(tokens []string) []Item {
	stack := make([]Item, 0)
	item0 := make([]Item, 0)
	stack = append(stack, item0)
	item := ""
	for _, token := range tokens {
		if token == "[" {
			top := make([]Item, 0)
			stack.Push(top)
		}
	}
	return stack
}

func deserialize(s string) *NestedInteger {

}

func main() {

}

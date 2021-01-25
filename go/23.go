/*

https://leetcode.com/problems/merge-k-sorted-lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

*/

package main



import "fmt"


type ListNode struct {
    Val int
    Next *ListNode
}


func mergeKLists(lists []*ListNode) *ListNode {
    if len(lists) == 0 {
        return nil
    }
    rmDict := make(map[int]bool, 0)
    for i, e := range lists {
        if e == nil {
            rmDict[i] = true
        }
    }
    newLists := make([]*ListNode, 0)
    for i, e := range lists {
        if _, ok := rmDict[i]; !ok {
            newLists = append(newLists, e)
        }
    }
    lists = newLists
    dummy := &ListNode {Val: 0, Next: nil}
    cur := dummy
    for len(lists) > 0 {
        minVal, minPos := int(2 << 30 - 1), -1
        for i, e := range lists {
            if e.Val < minVal {
                minVal = e.Val
                minPos = i
            }
        }
        cur.Next = lists[minPos]
        cur = cur.Next
        lists[minPos] = lists[minPos].Next
        if lists[minPos] == nil {
            lists = append(lists[:minPos], lists[minPos + 1:]...)
        }
    }
    return dummy.Next
}


func main() {
    lists := []*ListNode {
        &ListNode{Val: 1, Next: nil},
        &ListNode{Val: 2, Next: nil},
        &ListNode{Val: 3, Next: nil},
        nil,
    }
    head := mergeKLists(lists)
    for head != nil {
        fmt.Println(head.Val)
        head = head.Next
    }
}



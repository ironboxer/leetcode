/*

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

*/

package main


import "fmt"



type ListNode struct {
    Val int
    Next *ListNode
} 

/*
func deleteDuplicates(head *ListNode) *ListNode {
    dummy := &ListNode{Val: 0, Next: head}
    cur := dummy.Next
    for cur != nil {
        next := cur.Next
        if next != nil && next.Val == cur.Val {
            cur.Next = next.Next
        } else {
            cur = next
        }
    }
    return dummy.Next
}
*/


func deleteDuplicates(head *ListNode) *ListNode {
    dummy := &ListNode{Val: -99999999, Next: head}
    cur := dummy
    for cur.Next != nil {
        next := cur.Next.Next
        for next != nil && next.Val == cur.Next.Val {
            next = next.Next
        }
        if cur.Next.Next != next {
            cur.Next = next
        } else {
            cur = cur.Next
        }    
    }
    return dummy.Next
}


func main() {
    head := &ListNode{Val: 1, Next: nil }
    head.Next = &ListNode{Val: 1, Next: nil }
    head.Next.Next = &ListNode{Val: 1, Next: nil }
    head.Next.Next.Next = &ListNode{Val: 1, Next: nil }
    head.Next.Next.Next.Next = &ListNode{Val: 2, Next: nil }
    head.Next.Next.Next.Next.Next = &ListNode{Val: 3, Next: nil }

    cur := deleteDuplicates(head)
    for cur != nil {
        fmt.Println(cur.Val)
        cur = cur.Next
    }

    head = &ListNode{Val: 1, Next: nil}
    head.Next = &ListNode{Val: 2, Next: nil}
    head.Next.Next = &ListNode{Val: 3, Next: nil}
    head.Next.Next.Next = &ListNode{Val: 3, Next: nil}
    head.Next.Next.Next.Next = &ListNode{Val: 4, Next: nil}
    head.Next.Next.Next.Next.Next = &ListNode{Val: 4, Next: nil}
    head.Next.Next.Next.Next.Next.Next = &ListNode{Val: 5, Next: nil}

    cur = deleteDuplicates(head)
    for cur != nil {
        fmt.Println(cur.Val)
        cur = cur.Next
    }


}


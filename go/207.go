/*

https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5

*/

package main


import "fmt"


func canFinish(numCourses int, prerequisites [][]int) bool {
    graph := make([][]int, numCourses)
    degree := make([]int, numCourses)
    for i := 0; i < len(graph); i++ {
        graph[i] = make([]int, 0)
    }
    for i := 0; i < len(prerequisites); i++ {
        item := prerequisites[i]
        a, b := item[0], item[1]
        graph[b] = append(graph[b], a)
        degree[a]++
    }
    counter := 0
    queue := make([]int, 0)
    for i := 0; i < numCourses; i++ {
        if degree[i] == 0 {
            queue = append(queue, i)
        }
    }
    for len(queue) != 0 {
        node := queue[0]
        counter++
        queue = queue[1:]
        dep := graph[node]
        for _, v := range dep {
            degree[v]--
            if degree[v] == 0 {
                queue = append(queue, v)
            }    
        }
    }
    return counter == numCourses
}


func main() {
    numCourses := 2
    prerequisites := [][]int{
        {1, 0},
    } 
    fmt.Println(canFinish(numCourses, prerequisites))

    numCourses = 2
    prerequisites = [][]int{
        {1, 0},
        {0, 1},
    }            
    fmt.Println(canFinish(numCourses, prerequisites))
}


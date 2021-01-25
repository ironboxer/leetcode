/*

https://leetcode.com/problems/course-schedule-ii/

There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.

*/

package main


import "fmt"


func findOrder(numCourses int, prerequisites [][]int) []int {
    graph := make([][]int, numCourses)
    for i := 0; i < numCourses; i++ {
        graph[i] = make([]int, 0)
    }
    degree := make([]int, numCourses)
    for i := 0; i < len(prerequisites); i++ {
        item := prerequisites[i]
        a, b := item[0], item[1]
        degree[a]++
        graph[b] = append(graph[b], a)
    }
    queue := make([]int, 0)
    for i := 0; i < len(graph); i++ {
        if degree[i] == 0 {
            queue = append(queue, i)
        }
    }
    res := make([]int, 0)
    for len(queue) > 0 {
        node := queue[0]
        queue = queue[1:]
        res = append(res, node)
        for i := 0; i < len(graph[node]); i++ {
            e := graph[node][i]
            degree[e]--
            if degree[e] == 0 {
                queue = append(queue, e)
            }
        }
    }
    if len(res) == numCourses {
        return res
    }
    return []int{}
}



func main() {
    numCourses := 4
    prerequisites := [][]int{
        {1, 0},
        {2, 0},
        {3, 1},
        {3, 2},
    }
    fmt.Println(findOrder(numCourses, prerequisites))
}

/*

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.


*/


package main


import "fmt"



func max(a, b int) int {
    if a >= b {
        return a
    }
    return b
}


func maxPoints(points [][]int) int {
    res, N := 0, len(points)
    for i := 0; i < N; i++ {
        dup := 1
        for j := i + 1; j < N; j++ {
            cnt := 0
            x1, y1 := points[i][0], points[i][1]
            x2, y2 := points[j][0], points[j][1]
            // 说明输入的数组中有多个数据落在了同一个点上
            // 说明输入的数组中有重复的存在
            if x1 == x2 && y1 == y2 {
                dup++
                continue
            }
            for k := 0; k < N; k++ {
                x3, y3 := points[k][0], points[k][1]
                // 说明3点共线
                if x1 * y2 + x2 * y3 + x3 * y1 == x3 * y2 + x2 * y1 + x1 * y3 {
                    cnt++
                }
            }
            res = max(res, cnt)
        }
        res = max(res, dup)
    }
    return res
}


func main() {
    points := [][]int {
        {1,1},
        {3,2},
        {5,3},
        {4,1},
        {2,3},
        {1,4},
    }
    fmt.Println(maxPoints(points))
}

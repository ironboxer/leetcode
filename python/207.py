"""
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

"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        # res用来记录那些没有出现循环依赖的节点
        res = []
        matrix = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        for i, j in prerequisites:
            # j被i依赖
            matrix[j].append(i)
            degree[i] += 1
        # 没有任何依赖的节点
        queue = deque()
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
        while queue:
            i = queue.popleft()
            res.append(i)
            # 遍历所有依赖i的那些节点
            for v in matrix[i]:
                # 将该节点的依赖数量-1
                degree[v] -= 1
                # 如果不再依赖任何其他节点
                if degree[v] == 0:
                    queue.append(v)
        return len(res) == numCourses

# 判断一个图是否存在环

"""
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

"""

from typing import List
from collections import deque, defaultdict


class Solution0:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        degree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            # b refer to a
            degree[b] += 1
            graph[b].append(a)
        queue = deque(i for i, e in enumerate(degree) if e == 0)
        while queue:
            node = queue.popleft()
            res.append(node)
            for v in graph[node]:
                degree[v] -= 1
                if degree[v] == 0:
                    queue.append(v)
        return res


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = {i: set() for i in range(numCourses)}
        depes = defaultdict(set)
        for i, j in prerequisites:
            # 邻接表
            # i rely on j
            graph[i].add(j)
            # j reliad by i
            depes[j].add(i)
        # i 不依赖于任何其他节点
        queue = deque(i for i in range(numCourses) if not graph[i])
        while queue:
            node = queue.popleft()
            res.append(node)
            # 所有依赖node的其他节点
            for v in depes[node]:
                graph[v].discard(node)
                # 如果v不再依赖其他任何节点
                if not graph[v]:
                    queue.append(v)

        return res if len(res) == numCourses else []

if __name__ == '__main__':
    print(Solution().findOrder(2, [[1, 0], [0, 1]]))
    print(Solution().findOrder(4, [[1, 0], [0, 1]]))
    print(Solution().findOrder(2, [[1, 0]]))
    print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))


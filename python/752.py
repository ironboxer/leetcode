"""
https://leetcode.com/problems/open-the-lock/

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.



Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:

Input: deadends = ["0000"], target = "8888"
Output: -1


Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.
"""

from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deads = set(deadends)
        if target in deads or '0000' in deads:
            return -1
        visited = set(['0000'])
        from collections import deque
        queue = deque([([0,0,0,0], 0)])
        while queue:
            node, step = queue.popleft()
            node_str = ''.join(map(str, node))
            if node_str == target:
                return step
            for i in range(4):
                for j in [-1, 1]:
                    new_node = node[:]
                    new_node[i] = (node[i] + j) % 10
                    new_node_str = ''.join(map(str, new_node))
                    if new_node_str in visited:
                        continue
                    if new_node_str in deads:
                        continue
                    visited.add(new_node_str)
                    queue.append((new_node, step + 1))
        return -1


# 典型的BFS



class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque

        deads = set(deadends)
        if target in deads or '0000' in deads:
            return -1
        visited = set(['0000'])
        queue = deque([([0, 0, 0, 0], '0000', 0)])
        while queue:
            items, img, step = queue.popleft()
            if img == target:
                return step

            for i in range(4):
                up, down = items[:], items[:]
                up[i] = (up[i] + 1) % 10
                down[i] = (down[i] - 1 + 10) % 10
                a, b = ''.join(map(str, up)), ''.join(map(str, down))
                if a not in deads and a not in visited:
                    visited.add(a)
                    queue.append((up, a, step + 1))
                if b not in deads and b not in visited:
                    visited.add(b)
                    queue.append((down, b, step + 1))

        return -1


if __name__ == '__main__':
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    print(Solution().openLock(deadends, target))

    deadends = ["8888"]
    target = "0009"
    print(Solution().openLock(deadends, target))

    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = "8888"
    print(Solution().openLock(deadends, target))

    deadends = ["0000"]
    target = "8888"
    print(Solution().openLock(deadends, target))


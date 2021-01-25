"""
https://leetcode.com/problems/word-ladder-ii/

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""

from typing import List


class Solution0:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set(wordList)
        if endWord not in wordList:
            return []

        res = []
        visited = set()
        buf = [(beginWord, 0)]
        p = 0
        while p < len(buf):
            word = buf[p]
            for i in range(len(word)):
                for j in range(26):
                    new_word = word[:i] + chr(97 + j) + word[i + 1:]
                    # print(new_word)
                    if new_word not in words:
                        continue
                    if new_word in visited:
                        continue
                    buf.append(new_word)
                    visited.add(new_word)
                    if new_word == endWord:
                        res.append(buf[:])

            p += 1

        return res


class Solution1:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        from collections import deque, defaultdict
        words = set(wordList)
        if endWord not in wordList:
            return []

        res = []
        path = []
        visited = set()
        queue = deque()
        queue.append((beginWord, 0))
        while queue:
            word, level = queue.popleft()
            path.append((word, level))
            if word == endWord:
                d = defaultdict(list)
                for e, k in path:
                    d[k].append(e)
                print(d)
                res.append(path[:])
                path.pop()
                visited.discard(word)
            else:
                for i in range(len(word)):
                    for j in range(26):
                        new_word = word[:i] + chr(97 + j) + word[i + 1:]
                        if new_word not in words:
                            continue
                        if new_word in visited:
                            continue
                        queue.append((new_word, level + 1))
                        visited.add(new_word)

        return res


# 神搜会超时, 广搜会占内存

class Solution3:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set(wordList)
        if endWord not in words:
            return []

        res = []

        # 这个算法的时间复杂度是指数级别的
        # 指数级别的时间复杂度不能够忍受啊
        def f(word, path, visited):
            if word == endWord:
                res.append(path[:])
                return
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word not in words:
                        continue
                    if new_word in visited:
                        continue
                    # p = path[:]
                    # p.append(new_word)
                    # v = visited.copy()
                    # v.add(new_word)
                    # f(new_word, p, v)
                    path.append(new_word)
                    visited.add(new_word)
                    f(new_word, path, visited)
                    path.pop()
                    visited.discard(new_word)

        f(beginWord, [beginWord], {beginWord})
        res.sort(key=lambda x: len(x))
        for i in range(1, len(res)):
            if len(res[i]) > len(res[i - 1]):
                res = res[:i]
                break
        return res



class Solution5(object):
    def findLadders(self, beginWord, endWord, wordList):

        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord: 
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww]+=[j+[neww] for j in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return res



# 这个解法背后的思路是什么

class Solution4:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        from collections import defaultdict
        words = set(wordList)
        if endWord not in words:
            return []
        res = []
        layer = {beginWord: [[beginWord]]}
        while layer:
            new_layer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    res.extend(k for k in layer[word])
                else:
                    for i in range(len(word)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = word[:i] + c + word[i + 1:]
                            if new_word in words:
                                new_layer[new_word] += [j + [new_word] for j in layer[word]]
            words -= set(new_layer.keys())
            layer = new_layer
        return res


class Solution:
    def findLadders(self, beginWord, endWord, wordList: List[str]) -> List[List[str]]:
        from collections import defaultdict
        words = set(wordList)
        if endWord not in words:
            return []
        layer = {beginWord: [[beginWord]]}
        # 本质上还是一个BFS
        while layer:
            new_layer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]
                else:
                    for i in range(len(word)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = word[:i] + c + word[i + 1:]
                            if new_word in words:
                                new_layer[new_word] += [w + [new_word] for w in layer[word]]
            words -= set(new_layer.keys())
            layer = new_layer
        return []


# 到底是一种怎样的思路呢?


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(Solution().findLadders(beginWord, endWord, wordList))

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    print(Solution().findLadders(beginWord, endWord, wordList))

    beginWord = "qa"
    endWord = "sq"
    wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar",
                "ci", "ca",
                "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or",
                "rn", "au",
                "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh",
                "co", "ga",
                "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la",
                "st", "er",
                "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr",
                "sq", "ye"]
    print(Solution().findLadders(beginWord, endWord, wordList))

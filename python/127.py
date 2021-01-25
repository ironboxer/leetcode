"""
https://leetcode.com/problems/word-ladder/

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.


"""

from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        from collections import defaultdict
        bucket = {beginWord: [[beginWord]]}
        while bucket:
            new_bucket = defaultdict(list)
            for word in bucket:
                if word == endWord:
                    return len(bucket[word][0])
                else:
                    for i in range(len(word)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = word[:i] + c + word[i + 1:]
                            if new_word in words:
                                new_bucket[new_word] += [w + [new_word] for w in bucket[word]]
            words -= set(new_bucket.keys())
            bucket = new_bucket

        return 0


# 为什么这段代码是快的?


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(Solution().ladderLength(beginWord, endWord, wordList))

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    print(Solution().ladderLength(beginWord, endWord, wordList))

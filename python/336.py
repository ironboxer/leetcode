"""
https://leetcode.com/problems/palindrome-pairs/


Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.



Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]


Constraints:

1 <= words.length <= 5000
0 <= words[i] <= 300
words[i] consists of lower-case English letters.

"""



from typing import List

class Solution0:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        memo = {}
        def check(s):
            if s in memo:
                return memo[s]
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    memo[s] = False
                    return False
                i, j = i + 1, j - 1
            memo[s] = True
            return True

        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if check(words[i] + words[j]):
                    res.append([i, j])
        return res


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d = {w: i for i, w in enumerate(words)}
        ans = []
        for i, w in enumerate(words):
            if w[::-1] in d and d[w[::-1]] != i:
                ans.append([i, d[w[::-1]]])
            if w != '' and w[::-1] == w and '' in d:
                ans.append([i, d['']])
                ans.append([d[''], i])

            for k in range(1, len(w)):
                s1, s2 = w[:k], w[k:]
                if s1 == s1[::-1] and s2[::-1] in d:
                    ans.append([d[s2[::-1]], i])
                if s2 == s2[::-1] and s1[::-1] in d:
                    ans.append([i, d[s1[::-1]]])

        return ans


if __name__ == '__main__':
    words = ["abcd","dcba","lls","s","sssll"]
    print(Solution().palindromePairs(words))

    words = ["bat","tab","cat"]
    print(Solution().palindromePairs(words))

    words = ["a",""]
    print(Solution().palindromePairs(words))

    words = ['babababbbaaa', 'bbaabbbaabbbbba', 'abbbbbbbbbbbb', 'bbabaaababb', 'aabbbaaaababbbbba', 'aabbababbab', 'abaaa', 'aba', 'abaab', 'aabbbababa', 'aabbaabbbaaabaa', 'abbbbababbbbaaa', 'bbabbbaababbab', 'a', 'bb', 'ababbaa', 'baaba', 'b', 'bbaabaabaa', 'abbaaabbbbabbaabaabb', 'aabbbbaaaa', 'aabbbbaaaaab', 'abbaaababbaaa', 'abaaaaaabbabbaa', 'baaaabaaabaaa', 'aaaabaabbabaababaab', 'aaabbbbaaaaabbb', 'babaabbbababbb', 'babbbb', 'bababaabbbbababaaba', 'aaaaa', 'baabbaabbbabb', 'baaabababbb', 'bbbabbaaaabaaabbbba', 'aaabbbabbaaababaa', 'babaaa', 'baabbabbbaabbaba', 'bbb', 'baabaababba', 'baabaaaabaaababababa', 'bbbbbaaabaaabaab', 'abba', 'baaaaaababbbb', 'bbabbbbbaaaaaababa', 'aaaaabbababbbba', 'abaabbbaabbabaabba', 'babbaabbaabbbbaa', 'aabbabba', 'abababababaabaabab', 'baab', 'baabaaaaaaaa', 'baaabababbbbbabba', 'bbaaabbaa', 'bbabba', 'bbbabbaab', 'baa', 'ab', 'baaaa', 'aaa', 'abbaabab', 'aabbbbbbaaaaa', 'aaaab', 'bbabaaab', 'bbaabaabababaaaaabb', 'aaaaaab', 'aabbbb', 'baaabbabaab', 'abaa', 'bbabbaabbabbbbbbb', 'aabbabbbabbab', 'abbbbbba', 'bbbbbaabaab', 'bbbbbaabbbbb', 'abbbbbbbabbbabb', 'aaaaaaababb', 'bababbbbbabbabb', 'aabababbabaaababaa', 'bababa', 'baabbabaabb', 'babbbbaabab', 'aabbbaaabbbbabaabb', 'abaabbbaaaaabababbab', 'abb', 'bbaab', 'abbaaa', 'abbbbaba', 'bbaabaa', 'bbbabbaabbaaa', 'bababab', 'baaaabbbb', 'abbbbaaaaaba', 'aaabaaabbaabaaabbaab', 'bababbaababb', 'aaaaab', 'aababbbbbababbbaab', 'aa', 'bbaaa', 'baaababaab', 'aabbaaabba', 'abbaabbaaaababbaaaaa', 'babaabaabbabbaaaaabb', 'bbabaabbaababaabbaaa', 'abbba', 'aaab', 'baabab', 'bbbbbbaabbaabbb', 'bbbabbabbaabbbabbab', 'bbabbabbbabbabbbba', 'abaabaabbabbabab', 'abbbbbaaababbbbbbbb', 'aaaaababbaaaaa', 'bbaababa', 'aabbbbbaba', 'baabababbbaba', 'aaabbbbba', 'aab', 'baaabbbbaabb', 'bbaaba', 'abaaaaaba', 'bba', 'bbabaaaab', 'abbabaaabba', 'abbabbb', 'baaabbaaabbbbbbaabb', 'aaababbb', 'aabbbbabaabaa', 'baaaaaaabab', 'baaaabbaaabbb', 'abbaaaabbbbbbb', 'bbaabbabbaabbaa', 'baababbbbabaababbaa', 'bbababbbbbab', 'baabbbabbbabab', 'aabaaabababaaa', 'bbbbaaabaaa', 'bbbabbabb', 'abababbaa', 'abbbbbbaababab', 'aabbbbabaa', 'abbabaabbaaababbbba', 'baabbabbbaaabbbbbbba', 'bbbb', 'aababbbabaabbaab', 'abbab', 'babb', 'aabaabbaabbababaa', 'aabbbbaaa', 'bbbab', 'baabbabbabab', 'baabbbabababba', 'abaaabbaababbabb', 'aababbaaabbbbbbbaaaa', 'aaabaabbbbbbbbaaa', 'baaabbbbaa', 'babaabaabbabaabbb', 'aaaabaaaba', 'bbababbbbbba', 'bbaaabaa', 'bbbaabbabaaaa', 'babbbab', 'abbaabbabababbbaa', 'bab', 'aabababbabbbbab', 'abbbabababb', 'baaabbaaab', 'babbbaab', 'baaabbbbbbbaab', 'abbbaaaaaab', 'aababbba', 'bbbababbbbaabaaabba', 'babbaabbb', 'bbaaabaabbb', 'baaabaabbbbbaa', 'baaaaaab', 'babbaabbbaabba', 'aabbbbaaabbabbbb', 'baaababaabbbabab', 'aaaabaab', 'baabbaaabbaaabb', 'aabaabaababbabaab', 'aabbaba', 'baaababbabbaaabbabb', 'aabaababaaaaabbbabaa', 'ababa', 'babbbbbbabaaabaabb', 'babbaaaabbbbaab', 'abbbabaababa', 'aabaaaaabbbbabab', 'aaabbbaabaaab', 'aababbaaaaaaaabbb', 'aaaabbababaab', 'aabababbabbbbbb', 'bbbbbabbbabbb', 'aabbaaaaaabbbba', 'abbabaababba', 'aaaaabbba', 'baaaaaaaabbbbbbbb', 'aaaabbbabb', 'abbbabaaa', 'aaabbabbabaabbaaa', 'bbaabaabbbbbbbbbaba', 'bbaaabbababaaba', 'baaabbaaaaaabbbbba', 'bbabbabbabbbbaab', 'aaabaaa', 'bababaaabaa', 'aabab', 'babbaba', 'aabbabbbaab', 'aaaabaaabbaaaabaa', 'bbaba', 'bbabbbaabbbbbabb', 'bbaabbaaaaabaab', 'ababbbaababbab', 'babaaab', 'babababba', 'abaaaaaaaaaab', 'aabbb', 'abababbbaabbaabaa', 'aaaabbaaabbbbaabaab', 'aababababbaababbb', 'babbaaaababaa', 'aabbabbaababbaaaba', 'aabbbabaababbab', 'abaaaab', 'babbbbbaaaababaaabba', 'bbbbababaabaaabaaba', 'aaabaabbbaabaabab', 'aaababbbaba', 'aabaaabba', 'aabbaabb', 'aaabbbabbabaaaabbbb', 'baabbbaabaabaabb', 'aaaabbbbababbabbabb', 'abbaabb', 'baaaabaaababababbba', 'aabababba', 'baaaaaabbbabbbbaa', 'babbab', 'aaabaaaaabbaaaaaba', 'aabbaaa', 'aaba', 'aababbababab', 'baabaabbaababbab', 'abaaaabba', 'bbaaaabbaabaaa', 'babbaaaabbbaaabaa', 'bbaaabbabaaa', 'abbabbaaabbabbbabba', 'aaabab', 'baaa', 'ba', 'bababbaab', 'aabaababb', 'bbabaaaaaaabbabb', 'aaaabbaaaaaabbbababb', 'aabbabbba', 'abbaaba', 'ababbaababbbbaaab', 'aabbabbaabba', 'aaaaabaabababbbabbb', 'bbaababbabaabbb', 'babbabaaaa', 'abbbbabaabb', 'bbaaaabaabbbbbb', 'abaaaaaaababbaaab', 'abbaaaabaaababba', 'ababbaabbaa', 'bbabaabbaaa', 'aababaaabab', 'ababaaabbabaabbbab', 'bbbaaa', 'aababbbabab', 'aaabaab', 'bbbbbbaaabbabbb', 'baaaabb', 'abaaabb', 'bbabbabbb', 'bbbbba', 'bbababaaababbbbaa', 'bbabaaba', 'bbaabaabaabbba', 'bbababaaabaaaba', 'bbbbbaabbaaaaaab', 'babaabaaaaaabaabaaab', 'baabbababa', 'bbaabbaaabbbbb', 'baabbaaabbabba', 'babbababaaaba', 'babbbbbbababbbabbbb', 'ababaabaaabbbb', 'aabbbaabaabbabb', 'bbabbababbabbabb', 'bbaabaaaabbbbb', 'bababba', 'aaaaababbbab', 'bbabbbaaababa', 'abbababbaabaabba', 'abaabaabbba', 'babbbbaaab', 'bbbbabbaababbabbbaab', 'ababaabababa', 'ababaaa', 'abbbaabaaaabaaaaab', 'aaaabbabbbaaaa', 'abaabaaaabbabb', 'bbbabaaab', 'bbaa', 'bbbaaababbabbbaabbbb', 'abbababbbbaabaaabb', 'babaa', 'bbababaaaababb', 'aaaaaabbbbbbbaabbb', 'bbbbabbab', 'aabbababa', 'babbbabbaab', 'bbbababababbbab', 'baaaabbaaaabbabbba', 'baaaaaa', 'abbbbaaaaaaaabbb', 'aabaaaab', 'aabb', 'bbaaab', 'abaabba', 'bbabbbbbaaaaabaaab', 'bbabbb', 'baabaaabbbbabaaabb', 'aaabababaabababbaaba', 'abab', 'babbabababbbabab', 'abbabbbbaabbaab', 'aaaabbbabaaba', 'babaaabababbaabaaabb', 'babaab', 'bbabbbbba', 'abbaabbbbaab', 'baaaaaaa', 'baaaab', 'bbbabaababbabaab', 'abaaaaaabababbab', 'aaaaaababbbaaaaabbb', 'baaaababaabaaabbbabb', 'abbaabbaabbb', 'bbaaaabbaabbaaabab', 'abaaaaba', 'abbbabbbabbaba', 'bbaabbabbabababbbaab', 'baabaabbbab', 'bbaabababbaaaaabaaa', 'aabaab', 'abbabab', 'bbabbbbbabb', 'baaabaaaabaabaaba', 'babba', 'aaaaaaabaaaaaabb', 'aabaa', 'aabaaabaaa', 'baaabaabbbbaabbaa', 'bbaabbbbbabbbababb', 'bbabbabaaa', 'bbabaaaabbaaaa', 'ababbb', 'aaabaaabbabaaaabaaaa', 'baba', 'aabbabbbaa', 'bbabaababbb', 'aaabb', 'aababaabababbbaba', 'bbabbbbbabba', 'baaabbbab', 'aaabbbbbbba', 'baabbbaababb', 'aabababa', 'aababaab', 'aabaaab', 'bbbabba', 'babaaabaaaaabbba', 'baabbaabbaabb', 'aaabaaababbbabaa', 'babaabaaabaaabba', 'bbbbabaaaaabbbab', 'aababaabaaaa', 'abaabbbbaababaaaabb', 'abbbabaa', 'abbbbbbbbbbbbbbbab', 'abbabbabbabbb', 'baaaabaab', 'bbabababababb', 'baabb', 'abbabaaabbabaaabbbaa', 'aaaabbababaaaabba', 'babaaaaa', 'abbabbbb', 'aabbaa', 'babaabbabbbabaabaaab', 'abbaaaa', 'baaab', 'bbbbbbbaba', 'babaabbabaaab', 'baaaabbbbbb', 'bbbbbbbaabbbbaaaaaa', 'bbbbabbba', 'aaababbbbaabaaaba', 'babbbbb', 'bbabab', 'baaabaabbbababb', 'baabbaaaaaaa', 'bbabaaaabbaa', 'baabbbbbaa', 'bbababbbbaabababa', 'aaabababb', 'bbaaaabbbbbabbbabab', 'aaabbbab', 'aaaaaaaaabbbbbaaaba', 'aaabaaabbababa', 'abaabbaabbabaabbab', 'aababbaaaaaaabbabb', 'aabbbbabba', 'bbababaaaaababbab', 'bbbbaaabbaa', 'aaaabaa', 'aaabaaaaaababbbba', 'bbbaaaaabbbbbabbabaa', 'baababaabaabbbb', 'abbbaaabaabaaab', 'aabaaabbbbaaabbaab', 'aabaabbaaaaaaaaaaa', 'baabababbb', 'bbbbbaabaaaabaababbb', 'abbaabbaba', 'babbbaaabbaab', 'baaaabaaa', 'aababbbaabba', 'bbbabaaa', 'aabbaaaaaaaaab', 'baaaaabbaaabaa', 'bababbbbabbaaaaa', 'bbbabbabaabaaaaabb', 'aaaaaaaaabbaababbb', 'aaaabb', 'bbbbaaabaabbbbaab', 'bbbaabbabbbbbbbbabb', 'abbaaaaaaaabba', 'abbaaaaaabbbbbb', 'aababbbbbaabaabbbb', 'aaaaababaabaab', 'baaababbabbba', 'bbbbbabaabbbaa', 'aaaaabaabbbbbbbab', 'aabbbbbb', 'abbb', 'bbbaaaabbababbabbb', 'bbabaabaabba', 'abaaabbbaaaabbb', 'ababbbbabbb', 'aaaabbbaaaaaabb', 'bbaabbbaaaaab', 'abbaabbabaab', 'babbba', 'abababbabbaabba', 'aabbababbbaabba', 'abbbabaabaabbbaa', 'baaaabbaaaa', 'baabaa', 'abaabbabbbaabbaaab', 'bbbbaabbbaabbbbab', 'abbbbbbaaabaababb', 'bbbaaababbaabb', 'bbaaabaabaabbbaaabb', 'babab', 'abbbbbbbbbbbbb', 'abaaba', 'bbabbababbbbbbaab', 'baabababbbb', 'abaababbabaa', 'aaaaaabbaab', 'babbbbbbbbbbbaaa', 'aabbba', 'babaaababbbbbbbaa', 'ababaaababbaba', 'bbaaababbbaababa', 'aaaabaaaaaaaab', 'bbababba', 'abaaababbb', 'bbabbabbbab', 'bbbbabbabb', 'babbabbaaabbbbaa', 'bbbbabaaaab', 'aaabbaaaabbb', 'baaabaab', 'aabaabbbbbaaba', 'baabbabaabba', 'abbbbaabababaabaaab', 'aabbabaab', 'aaabbbbb', 'bbbabbbbbabb', 'abbbb', 'baaababa', 'babababbbb', 'bbabbbbbaabbab', 'abbabaabaaaa', 'bbbaa', 'ababbbb', 'aabbbaab', 'aaabaaaabbbbaabab', 'abbbbbbabaabaababaaa', 'bbaabbba', 'babbababaaab', 'bbaabababbabbbbbbab', 'ababbbabbabaabaa', 'aabbaabbb', 'aaabbbbabaabaabb', 'babbaaaaaababb', 'abaaaabaaaabbaab', 'aaabaababaabbaabbaab', 'aaabbbbbbbbaabbbaab', 'aaababababaabaaa', 'aaabbababbaaaaaababb', 'baabbb', 'abaabaaaabb', 'abbabbaabaabbb', 'baaaaaabbbbbab', 'aabbabaabab', 'bbaaaaaaaaabaaaaaabb', 'abaabbbaaabaaababb', 'babbaaabbbb', 'bbabb', 'babaababbaaabbaaaba', 'babbbabaaaab', 'abaabbababababbaaaaa', 'abbaabaabababbb', 'aabbbabb', 'aabbbaabbbbaaaabba', 'babbabbbaaaababaabba', 'bbbbbbaabbabbbbabba', 'bababaaababbbababaa', 'bbaababbabaaaa', 'bbba', 'abababaabaababaabb', 'aabbbbabaababbab', 'abbaba', 'babaaaabbbababa', 'abbbaab', 'ababaaaaabbabbb', 'bbabbbbbabaabaabbbba', 'aababab', 'abaaaabbababbaab', 'bbaaabbbbabaab', 'aababbbaa', 'aababbbabbababbbbaba', 'baabaaaaaabab', 'bbbababbbbab', 'baaabbbaabaabbb', 'aaaaabababaaaaabb', 'abababbbaaaabbab', 'bbbabaa', 'abaaabbbabbaaaabbbbb', 'bbbbbbbab', 'bbbabbbbaababba', 'abbbabababab', 'abbbbbbbaaaaaabbabbb', 'aaaaaabaaabbbabab', 'abbaaaabbbababbbaa', 'bbbbbbaabbbaababaa', 'baabababababbbaaba', 'baaaaaabbabbaabbbaba', 'aaabaaabababbabaaaab', 'aababbababbabab', 'abaaababa', 'bbababaabbbabb', 'abbbababbb', 'bbabbabbaabab', 'aabbaabaabbbabb', 'bbbabab', 'baaaaabba', 'aaaabbabbbb', 'babbbaaaaa', 'babbaaa', 'baaababbaab', 'abaaabbaaaaabaab', 'abbbaaabaabaabaa', 'baababbbbaaaba', 'aaaaabbbbaababaa', 'babbbaabbbbabbbbabaa', 'bbaabaabbaabbbb', 'aaaaaabaaaaaaabbaa', 'abbbbbaaba', 'bbaaaaabbabaabba', 'aaabbbaababaaaabbbbb', 'bbabbababaaababaa', 'bbbabbaaabaaababaa', 'babbabbbb', 'abbbaabb', 'aabbbaabbbbbbaa', 'aabbbbbaabbbbaaaaba', 'baababbbbabbaa', 'abbabb', 'baabaaabbabbbabaa', 'aaaaababab', 'aaabbbbbbbbbb', 'bbaaaabbbabbbba', 'aaaabababab', 'abaaaabaaab', 'bababbbaa', 'abbbbbabaa', 'bababbababbabbbbb', 'aabbaaaa', 'abbbbbaab', 'aaaabbbaabbbab', 'aaabaaaabaa', 'ababbbbbbaababbabba', 'baabbabbaaba', 'abaabbaaab', 'aaabbaabbaabbaaaaba', 'baabba', 'aabbbaababbaaabaaaba', 'babaaaabbbab', 'aaaaabbbbbaaaa', 'bbbabbaabbb', 'bbbbaabbabbaababbbbb', 'baabbaa', 'aaaaba', 'aabaabaaababbbaa', 'bbaaaaabab', 'ababbababbabbaaa', 'ababbbaaaab', 'babbaababaaaabbabb', 'aabaaaabaabbabaaa', 'abbabaaabbabb', 'abbbbabbbbbb', 'babaabaa', 'bbabbaabbabb', 'baabbabbbaba', 'bbab', 'bbababaabb', 'bbabbaaabbaaa', 'ababbabbabaaaab', 'bbabababaaaabababb', 'baaababbbababbbbba', 'bbbaabaabbaabbaba', 'aabababbaaaba', 'bbbaaaabaabbaababaab', 'bbbaaaabbbabababa', 'bbaabab', 'baaabbaabbaaaababba', 'aaaabbbbbaaab', 'baabbbabbab', 'abbaaabaaab', 'baabaaa', 'bbbbb', 'aaaaabbabaaaaaabbbba', 'aaabbababbbaabbaaab', 'aababbaabaaabbbbaba', 'bbbbbbbaaaabbbbabbbb', 'abaabbabbaaa', 'baabaaaabbbabb', 'baabbaabbabbbbabbaba', 'aaabbabaa', 'bbaabb', 'babaaba', 'bbababaaaaaabbbaab', 'abababbba', 'bababbaaabbabbab', 'bbbbbaabab', 'bababbaababbaaababaa', 'bbbbaab', 'aaabababaa', 'abbaaaabbbaaab', 'aabbaaaabbaba', 'aaababbaababbbaabbbb', 'ababba', 'bbbababbabababba', 'abbbabaabbaabaab', 'aaabbba', 'bbbbababbaaaababa', 'aababababba', 'bbaabbbbabbaaa', 'aaaaaaabbbba', 'bbaabbbbabaaaaaaa', 'bababaaaabaab', 'aaaa', 'abbabaaabbbaabbb', 'baabbbabbaa', 'bbbabbbbaaabababaa', 'bababbbbbaaababb', 'bbbbbb', 'abbbbbbbaaabbaaab', 'abbbaaab', 'bbaaaababa', 'bbabaabbbababbbbbb', 'baabbbbbbaaabbab', 'abbbbbabbabaaaba', 'baabaabab', 'bbbababbbbbabaaaaaaa', 'abbaabbbbbabaaaab', 'abbbaabbabbabbbaab', 'bbbbbbabbbbaaaaab', 'abababababa', 'babaaaaaaaaaa', 'aababbbaabbb', 'abbabbbaaaabbbbbbbb', 'baaababbbbaaabaababa', 'baaabaabaababaaabba', 'bababbababbbaabb', 'abbabbaabba', 'babaabbaaaaabbb', 'abbabbbbab', 'abbbba', 'abababaaabaabbaa', 'bbbba', 'bbabbbbaaaabbbaaba', 'aabaabb', 'ababbbaabbbaaababba', 'bbaaabaaaaabaabbbaa', 'babaaabbaaaabbbba', 'aaaabaabbbabbbbaba', 'aaaabbaaaabab', 'aaaabbabbaabaabaaab', 'bbabbabbaaab', 'babbbbaaaaaabbba', 'aabbabb', 'bbbbaa', 'baabbbaabaaaa', 'aababbbaabaabab', 'aabbbbbababba', 'bbbbbbabbbbbb', 'babaabbbaaaaabbbaa', 'bbbabaabbaa', 'bbbbaaabaaaba', 'abbbaabaaaabab', 'aabbbabbb', 'aaaabaaabbabbbbbbbaa', 'bbabaaaababaabaaaab', 'aabaaaabaaabbbaabbab', 'baabbbbabba', 'bbbaaababbbbabbaaaaa', 'aabbbaaaaa', 'bbaaaa', 'bbbabaaababaaaababa', 'aaabbbbaaabbbabba', 'aabaaabab', 'abbaabaaaabbbab', 'abbababbbbabbab', 'aaabbaaaaaaaba', 'aaaabab', 'aaaababa', 'aabbbbbbbba', 'bbbbbbbbaabbabaabb', 'bbaababaaabbaabab', 'abaabb', 'bbabaab', 'aaabaabbbababbb', 'bababbaaaa', 'aabbbbaabbababababbb', 'baabaabaabaaaab', 'babbaabaaaa', 'bbbaaabaabbbaaaabb', 'bbaabbbb', 'aaaaaa', 'abbaabbbbbbaaaaba', 'abbaabaab', 'abbbabbaaaaabaa', 'babaabaaaabbab', 'bbaabbaaababababbabb', 'baaabaaaab', 'babaaabbabaabbaabb', 'bbbbaaba', 'abbbaa', 'aaaabaabbba', 'aabbbbbabaa', 'bababaaaaaabba', 'baaabbabaabb', 'bababbbaabbabb', 'bbaabbbaaba', 'aaabaa', 'bbababbb', 'abaabbbbaaabaa', 'bbbaabbbab', 'babababbbaabba', 'bbabaaaaabaaa', 'abbbbbbb', 'bbbabababa', 'babbbbbababbabbbbab', 'baabbabaabbbbbbababb', 'baabbabbbabbaaaaa', 'abbbaabaab', 'baabbaabbabbbaabbba', 'aaabbbbbb', 'abbabbabbbbaabbaaba', 'ababaabbbbbaaa', 'aaaaabbabaaaababb', 'aabababaaaabb', 'bbbaaababbbbabbaa', 'bbababbaaa', 'aabbbabbbabbbbb', 'babababbabab', 'aabbbabababbbabbaa', 'abaaaa', 'bbaaabaaabbbabb', 'baabbbbbbabbbbbbaab', 'babbabababaabbaabaaa', 'ababb', 'bbbaabbaabbabaaba', 'aaaaaabbbbabaaaab', 'bbbbabaababbababab', 'bbaabaababbbbbaaabb', 'abaababbab', 'bbbbaaabbbabaababba', 'bbbbaababbbaaa', 'abaaaabbbabbaa', 'babbaaaaabb', 'bbaaababbab', 'aabbabbbaabaaaaab', 'bababaa', 'aaaaaaaaa', 'ababababb', 'bbaababab', 'abbabbaaabbbb', 'abbbaaaa', 'abaabbbaba', 'abbbbabaabbababbbb', 'baababbbabaaaaa', 'baaababaaaaaba', 'abaaabaaaa', 'ababbbbaabbaaaaaa', 'babaaabbba', 'aababbbaaabbabaabab', 'ababbbbaba', 'aababaaabbaaab', 'aaaaaaabb', 'ababaabaabb', 'bababbbaabbabba', 'abaaaba', 'bbbbaaaabbababbbb', 'abaaabbabbaabba', 'abaabaabaaabbbaba', 'bababababbb', 'abbaaabaaaabaaaabaaa', 'abbbababa', 'bbaabbaaaaaaaabbbbba', 'abbaaabbba', 'bbabbabbbaa', 'baababaaabaaaba', 'baabbaaabbabaaaabab', 'bababbabbbaaaabbaba', 'aaabaaba', 'aabbab', 'baababbbb', 'babbbbbabbabaa', 'aababaabaabbaabba', 'babaaabbbb', 'aaaabbaaabbabb', 'abaabaaaaababba', 'aaaababbabbbaaba', 'abaaabbaabbb', 'aabbbbbaabbaab', 'bbabbaa', 'abaaababbbbbbbaaabaa', 'aaaaabababaabaa', 'aabbbbaababaaabaaba', 'bbababaabbabbaaabbbb', 'aabaaaabbaaba', 'bbaabbabbbaaaab', 'baabaabbbbbbbbbaab', 'bbaaabbbbaabaaaa', 'abbbbbbabbababb', 'aababbbabbbbaa', 'bbaaaaa', 'ababbbaaababbababb', 'abaabbaabbabbb', 'aabbaab', 'aababbabaaabbbbab', 'baaaababaaab', 'babbbbbbabbab', 'abbbbbabaaababbaa', 'babbbaaaba', 'baabbbaaab', 'abababaaaabbbbbaab', 'bababababaa', 'bbabbaabbbbaaa', 'bbbabbab', 'aaaaaabbab', 'bbabaababaabbb', 'aaaaaaabbababbaabba', 'abbabaaaaaab', 'aabaaaa', 'abbaabbb', 'abaaabaabaaa', 'aababbbbbbaabaabbabb', 'bbbaaaaaabbab', 'aabbbbabababb', 'baabaaaabbabaabb', 'aaaaabbb', 'abbabbbbbba', 'bbbbbabbaaaabaabaaa', 'ababbaaaababaa', 'baaabab', 'aabbababbaababbb', 'baabbabbaaaaaa', 'babbbabbbaabbaba', 'aaabaabababaababa', 'babaabbaaaba', 'aaabbbabaaaaa', 'abbaaaabaabbbaa', 'bbaabbababbaaabb', 'aaaaabababaa', 'bbaabbababbbbb', 'abbbabbbbabaaaba', 'bbbaababaabaaaabaaaa', 'bbaaaababbbbba', 'abbbabaaabb', 'aababbbbabbaaa', 'abababaaaabbab', 'bbbbbbbbaaaaaaaa', 'aaaabbaaaabbbaabbb', 'aaaabababb', 'abbbbbabab', 'ababbbaaaaababaaaaab', 'babaaaa', 'babbabbbbbbbb', 'bbbabbaaabbbbbbba', 'abbbabbbaaaaaabbb', 'bbaabbbbbbbababab', 'bbabaaabbbbb', 'aaaaaabb', 'aaaabaaabbba', 'abbbaaababbaababaaab', 'aaaababaabbabbaab', 'aaababbbbbabbbabbba', 'aabababbbbbbbaababa', 'ababaabbabbbbabba', 'aabbabbabaaa', 'bbbababb', 'aabbaaabbabaaa', 'abaabbaabbbbbababb', 'aaaaababbaaabbaaaaba', 'bbbbaabaaabaaababb', 'bbbaba', 'abbabbbaabbabbbbaba', 'aaaababbaaaaabb', 'aabbbbababaabbbbaab', 'abbababba', 'abbbaaabaabbbabaaaab', 'bbbbbaabaaabaabb', 'aabbaabbaaaaabaaaaaa', 'abbabaaaaaaaba', 'bbababbbbbababaab', 'bbabababa', 'babbababaababbabbb', 'bbbbbbba', 'bbababbabbbabbabbaba', 'bbbbbaabbbabaaba', 'aaaababbababbabaabaa', 'bababaabbba', 'ababbbbbabbbaaa', 'abbbabbaaab', 'bbbabaaaa', 'bbbabbb', 'baaababbabaaabbaaba', 'bbbabaabbaaaabb', 'aabbbabaabaaabb', 'aabbabbbabbbabaa', 'bbbaaba', 'aabbabaabbababbaa', 'bbaabbabbab', 'bbaabaaaaabaabbaaaab', 'abbabbabbabbaba', 'abbabbbabaababbb', 'baabbbaabaa', 'aababaabaabbaaabb', 'babbbababbabbaab', 'aaabbaaaaabaab', 'aaaabbbabaaabaabaaa', 'bbabbbbbba', 'ababbbbaabaaaaaaaa', 'babbbbbbbbaab', 'bbbbbaabaaba', 'aababaaaabaaaaaba', 'babaaabababbaabbaabb', 'ababbabbaaabbbabbbaa', 'aabaaaaabba', 'bbbbabbabbababbb', 'ababaababbbbaaa', 'bbbbbbaaabaaa', 'babbabbbababaaaabbbb', 'bbabbbbb', 'abaaabbababbaaabbb', 'bbbaaabaaab', 'bbabaabbaba', 'bbbbababbbbbbbbab', 'baaaaaaaaabbabababab', 'babbbbabbaaabb', 'bbbaabb', 'babbaa', 'aabbabbaabbb', 'aabba', 'bbabbbbaabbbbbb', 'aababbbbbababbaabb', 'aaaabbbababbaaaaaaba', 'babbaabaaabbaaa']

    print(Solution().palindromePairs(words))

    words = ['ag', 'dadbcah', 'heeeahacdahj', 'feg', 'dadficbhih', 'ihdggfeefh', 'fbedcahdfeab', 'djaacjcfj', 'haijah', 'hbaebhd', 'd', 'cbedeei', 'gc', 'jddgeccbdhgdiccfdigb', 'edgchajgjbhch', 'djdebb', 'b', 'egiegejggbgi', 'acdjabiddcjce', 'dggeeffebiehdbgg', 'dbdefhgaejaghehcb', 'cjhgbgjecdfbddccjehf', 'bdgjage', 'ggfeggg', 'hajc', 'bjdgjhdedefifdihg', 'afhgdhacdjfa', 'iigadadg', 'gjadachfdiaejijdfdgd', 'fiaeajiaebahfjdagc', 'iagjfdfcghehfjia', 'afd', 'bgfgcajfhddajiceeaaf', 'iefcfgfdjecg', 'ebceadaaigdbc', 'igbcdbdfdjegff', 'jfabjebjge', 'hedchddj', 'eehgggbifbfbg', 'gjefdjfahib', 'hadgj', 'bfde', 'dg', 'bidedjffcdegh', 'gejbefeaiieidha', 'ajgcejcfgidafghdejdj', 'aafbcdh', 'hicif', 'fgidijdfbgjfacjcf', 'iciajjdiggejedgd', 'jjdfbedjifj', 'hhfbfh', 'bibbefhjbbbjjejjgi', 'egeigdhfbgfehfbhgbga', 'fiiddfegdahbajcaba', 'dfjfjebhdj', 'jg', 'hafahdbgijfjhafc', 'djafgehi', 'agbd', 'fgchciaeeidfjagefahe', 'jhifccfhbgechaefjbdb', 'bahfcecjjgejbibajd', 'idgdgcidigbedbafa', 'fddejfjddeeiga', 'jijhjcci', 'fbdedaciahjcicei', 'aababeiaeh', 'eideccaddgcicifd', 'ea', 'faehegabdgadc', 'fihajceafdd', 'cagbehagajc', 'cgje', 'ighdcefhe', 'cbbiaigci', 'ggfejebhbhfdbifb', 'bfabjjfjcegdbjebcjid', 'bcdgehfjdfdb', 'hdcihijbahfjcjdfb', 'jfjfhgjdjbgihgabjhbh', 'bfaaebjdj', 'acgbcjebedghfi', 'fdcehcgbgdchifjaahd', 'eiajbjfgec', 'eiigjidjjd', 'gbie', 'ihccaajfdjdjidceebi', 'eceegacbgigd', 'fff', 'bdjgfgggccgfbfbd', 'gchiafbbggdccgc', 'aefehccgcaccgd', 'cebhgac', 'jegcfegj', 'aggcdjic', 'egaejbejefch', 'ibfge', 'ejjhg', 'ijfhaibfhhd', 'chag', 'j', 'di', 'gieicbfai', 'hhbjaeeachdiijh', 'jicajhfhdjhbfhjicch', 'gbfjabfe', 'babddicdhdiigfjgcga', 'ihbgjfbgjh', 'ijbjbhgchhcdacgeig', 'bdbhigbfbebcah', 'hghgdich', 'hdd', 'aebjeh', 'cchadbg', 'gjdjjhihjg', 'cidibijif', 'cehefdedgdjdafg', 'hchca', 'ffdfbidfhchhe', 'edgjhcdib', 'cedcdgjdcggdajcbejib', 'gbjjjaiijjiijii', 'agdhfbgehfcidadd', 'acgfaacfgehhihibcbb', 'jfebeihiacgjggicgij', 'cbgadaiffjcj', 'abi', 'dbfehfffcaa', 'gdbeddaccffd', 'he', 'jdcfjjdceaf', 'bhabdahe', 'fiehffebffd', 'dhdgcechbdcbfj', 'efbiiaeahifda', 'jgjhijeegajd', 'dh', 'jigeijbcddhf', 'e', 'fahcehhhjhf', 'iffechadhjbbjgfgi', 'fccbgdeffjjhceh', 'jiefceggii', 'hhjhijiijihh', 'fibeb', 'cb', 'dgjcfdfbjjjg', 'ghcidcgjiicaab', 'cjhc', 'abh', 'hccajge', 'hagbjcjhhgahadabffj', 'ehccgaficdiajib', 'jiajgf', 'ch', 'fcehajcfafceafbdjea', 'adjdhcdjibh', 'decjbjecg', 'baeidjbbajjffiabgcjb', 'bjibfiij', 'edfa', 'jjiba', 'gcjijifd', 'edejihjahbjf', 'ehfdjfeebjgij', 'ecgbcebaacgiifgj', 'djgchbcjcfabfii', 'bbgahefbjiihfciifdc', 'edjhie', 'iaijicfdhdhiigiech', 'jeaiacicajdacabggghj', 'ffidgghe', 'fi', 'igcdigbcbhgfac', 'igdbhfhbheceagfhifec', 'fbgbabaadjfg', 'hejjjahed', 'fhfehgfibb', 'dcjecbccggeheeaddfh', 'dcgcjffagajfhb', 'gfj', 'aca', 'aegfifc', 'dgjbeijdhjagcfejeae', 'g', 'cfhhdfcde', 'gb', 'ijjaij', 'fcfdahjaadgf', 'cgddfddjcigc', 'ccjibdabg', 'ffg', 'bhgccdjaheiffge', 'dagdiahhe', 'ibefjebjgijggfbcd', 'gijcijaiifeddhjafg', 'ei', 'gbeiga', 'fbc', 'cffeigheehaecfefaf', 'hbfb', 'ebhehcaaafdgghacdcc', 'gfbjchdagjcdhiffeg', 'afciafahcggbfghabjcc', 'jdbgjb', 'gefaa', 'gfeifhdhaia', 'c', 'chjbfcde', 'ffbdjbda', 'hjcafagejecjbdeghbfi', 'hfejebjaffbi', 'f', 'bdjhddji', 'feafhche', 'jggjhibddejigjehah', 'caeddaace', 'caceb', 'acajhdebh', 'ggeadaa', 'dbeif', 'ihdifhijgcjbdijia', 'fibjfeecdchj', 'febihiaciahbii', 'gjcafcbgfejdcidag', 'bidgh', 'ajcacfhcjedjegi', 'ejfaghcebhhhicgcjfe', 'ccfbdafigibdeggg', 'dghd', 'efhfbfajea', 'ggfegichia', 'igccjieidbebcccicid', 'ggcb', 'gdbbdjdi', 'h', 'ebdeegcddc', 'fieebfbeeigcjcb', 'ijfdeibijbjeaa', 'jahahgcfidb', 'ejhdhjagi', 'jcfiddhjdcggeeedjjg', 'cgdcecffhgiceceafbgj', 'icgiaehcejabefbg', 'eiechjcjajdjjjcbhi', 'eefjcjggbjda', 'fihbiaafghbjacdggej', 'gaheadcdfefef', 'fcdjgggaagaccfhj', 'jbhbj', 'dbeadfjdgdhc', 'gdjcic', 'cifjdcfeedab', 'jacdggchfgfjf', 'edggieccfgfebicdh', 'ghfajadffjeicieg', 'fgdhgffgb', 'jicdgggahdhdhbi', 'bbgg', 'fhdhfjigbbjfejdhcc', 'haieafgdaabhiiifc', 'aajiagjhhhgeagehcdef', 'hgdafaehjiifdif', 'adebdcb', 'gecbgigc', 'dfdjjdccjdifggidhbbh', 'ji', 'acdhabebefdabdig', 'jjfhccbb', 'ieifihffcjgedegcie', 'efdhhghb', 'jic', 'iibjbccgi', 'ffffajgbbcgiaabdja', 'efifj', 'jfhghfcjccgdjhhaijf', 'ejbcfhgigge', 'jbhibci', 'igiejg', 'fhaj', 'hccfjiihdheihfgadjh', 'eeb', 'cahijghj', 'cdigbcbedcfjb', 'ciegfgdgeejcij', 'i', 'bjhjcbddggie', 'cdgjjdecbehb', 'ccgdcdbfgeccegaeacbb', 'ieejeb', 'iecdcbd', 'chii', 'fcbgfaibffjabjg', 'iidegjdigaiebeddjdh', 'gachcjabh', 'fijjebdefdhfgcjccbei', 'jediheaif', 'cdfihjgeegfdg', 'bdj', 'cebfejajgbg', 'ghcbdfieiigcdh', 'cfbjbg', 'ebfhfeigeghfi', 'chjihe', 'abeagebeffdifjg', 'hcebjgaffeehgfb', 'idhgjbcfjfbaj', 'hijbgbiebbcfgihbf', 'ijib', 'dcedeeidj', 'fbdjj', 'jciijbdjgbiahiefb', 'gfiaddehdgagba', 'jhbebgj', 'hfcbcejabbjbce', 'icdcccbddcjigdhbdfi', 'fdfbjcdifjdebdifff', 'fhcidafb', 'iccjhchahhheejcda', 'adfcbdgdaaeefbab', 'jbcfbg', 'bjdaicdjbjcgbcbbcbh', 'dice', 'fhhicbdeeahaibfhjf', 'ccdeabbfebjihbhgfag', 'bheaccdgfbjfjcjei', 'jjfiafba', 'cadcdeegbbcchii', 'ffdegjgjjadhe', 'ii', 'dcbhdaaeibdieijbcab', 'egbeegdffdcjjeegg', 'dcbihcfhigif', 'ijghbbhhfbbcdb', 'daajgfahdiifjhaifaif', 'ghdgjbfdhbafdab', 'iabfaejjfaie', 'bbbci', 'gfghfidach', 'fccafhidc', 'ebfbefg', 'jidbhidij', 'ihba', 'jciciehiffgjhijjjedc', 'gdacdjebffjeeie', 'hibdech', 'ci', 'dgce', 'bfdjdiffdgjdj', 'ffbajddhdi', 'aae', 'ffbigadaaa', 'gfgdfcaiadeaagbafb', 'caghbfhjddfeaedd', 'acfcebbjfhdjjde', 'idgdjbbe', 'dhc', 'cegg', 'aebcihdicbaggejef', 'djifcbbffeidhb', 'ieadcadcgjjdcbejbcae', 'baheaichgigfgfece', 'dhbfejcihgchii', 'badbbaceijdehe', 'ajghfjadicijabe', 'hfjifghcjdaifgcaej', 'ecceebeaigadj', 'bcbbbajigd', 'gjahfabebdd', 'ig', 'gjjefgajggidgjbg', 'igcdhddegcccbiagjc', 'bibjddacghi', 'hegbiahdjgegdibc', 'dhchfcgcdhafejb', 'ffbfijceaf', 'fehd', 'fedadadbddahdeaecj', 'jdfdgddfihbcidh', 'gig', 'haceghcdcebbbfccdi', 'jaagbiieibebehb', 'eegjhebdd', 'a', 'degecadgiedecib', 'hfaejeeieaijabijb', 'hgciaef', 'fjehbde', 'cehedadfbhijh', 'ff', 'afef', 'cgfjhicbiafhcac', 'iebha', 'djgagdigbbegebidj', 'aajdcdhaihcac', 'hfecbjhhbgfa', 'jegifhi', 'jchgadbjghaifi', 'eccabiagg', 'aifccc', 'dhefcihcaf', 'df', 'adjidjidejedbbg', 'ffgicfidjgcbbcf', 'ggbicjaigbccfef', 'gccibedgfhbihbeajibj', 'daaehih', 'bh', 'jagiajijeic', 'jeacebgcj', 'iccff', 'jjeab', 'gjabifjhh', 'dahjfahacadajgiig', 'jfgihdah', 'ggfbfhdhjcbdhecj', 'bfeehccbgf', 'iaeigffd', 'ded', 'djgjcaejei', 'habibida', 'hfhhafaj', 'ghbheddcaagbjefg', 'geidbcihihihfi', 'jhjfjjifbdfaiaecjggi', 'acjd', 'ahbcjgddicj', 'ecfeebhfce', 'ajbbaegad', 'dhahcfjdaaeajahgacfh', 'jdhjhbiciechbghdcc', 'ifabaacdfjied', 'gdjdfcadfb', 'ecjebjhg', 'cbhebajfaaaegh', 'hjagd', 'ga', 'cfhdibcgfdeehhgjjiaa', 'jhegjbeidhaff', 'afgcjfebgjjdaebh', 'ifgjihbgecjjicif', 'ccbiefbjgdbefbaefad', 'db', 'jcdicigebheeieiafb', 'cjfhbbhgdbahdeja', 'afgbbdhed', 'cbegb', 'chhidjf', 'ibdgbedcfagbjd', 'cabfeicafced', 'aa', 'behj', 'cdghdhcifih', 'cgjfjbfdbjbijcffdf', 'ahfefejdfegec', 'fjbgdicifb', 'ggejjgafhegibg', 'fhaghihbfjgecah', 'ifejbjfecighefb', 'ijci', 'dhihdjjjcjdhjabjfei', 'abdedeigfb', 'gdjcefcibjeebdeb', 'eccdcbeagb', 'hgebcjcfcbcccbhid', 'eecacechbcecajj', 'fdjbdhhidbgcehigjfc', 'jeaihefgejjgjigi', 'dhcje', 'accccdigcdddceca', 'djjbcdccj', 'hjcgaibfjhjiaf', 'dhajjihdeff', 'hejebj', 'gehifc', 'jhcjabgibcaagecfjdfb', 'gdgfjcfc', 'egdh', 'jgej', 'did', 'ehjbaifiaa', 'ceihedadgbhahhe', 'edcegedhh', 'ihedc', 'jcaeaicgfjj', 'jcgfcecbgcag', 'iiceeihedhfgbj', 'aajejefghheg', 'fcjee', 'fdbb', 'fcjfijhagjiecfa', 'jfbfedgagfedheb', 'hhiagi', 'jfgjadjiihjjefchha', 'cegida', 'jgegghhb', 'hbjbhhfjchfi', 'adbfcijdjbidg', 'icf', 'hjcgge', 'hieedgaaaffg', 'ajgageheebid', 'jdbebdc', 'aeaagf', 'dagccfcgeiid', 'hg', 'afceebiafjceadc', 'cfhaagebfc', 'fihdiff', 'jcajjhd', 'ddbdfjjdc', 'jbecijhdfbhcfjab', 'fggfgbafhjejd', 'hijadacifgdchegh', 'jid', 'adjhf', 'gadfcija', 'bdeidi', 'jfccehfhbecchgccg', 'gbbdbb', 'jidjhbdhcccdbdhcbbf', 'bgheejgddeejejej', 'hbhefdj', 'jacgi', 'fifjbfciiejbc', 'jieii', 'bafgacjifhighf', 'jcbhiaigcai', 'bhjeh', 'ghigdbbjcgiijjfcb', 'ijgffdheiaefebhgh', 'ghijeidgjggbb', 'hcfdacebgjgjf', 'cdfe', 'iehchadfeiada', 'dbg', 'ihjceafefh', 'fahehgbcejjfc', 'gdeaefgjgjedfdgha', 'jeh', 'ifd', 'jig', 'cgjhifgg', 'cddgibcdiiaecfiihgfe', 'cfjhibbccije', 'deeiafdie', 'bdedifdjghjjccegg', 'gcgfaejadida', 'idjeehhe', 'fadehe', 'abjjdddhfdfj', 'bicef', 'adcgdeagaijicghijhi', 'aggiididcbi', 'igfbibbjgh', 'bfjccccfjicgdbdgah', 'fcaciedhcbb', 'cjaiaehd', 'faic', 'hiaef', 'bjjhfjgdiidcbfbf', 'jacjheceg', 'djeejiehgh', 'bdjag', 'bfcfjigbjfcccbihj', 'jefdef', 'bjgcbahf', 'bbjidcbfgafhifheihc', 'hcajfcd', 'ifjhahbdahgacgdejg', 'cfjehhijfcdfeb', 'agffcfacib', 'jfagbaifeabbgjaaag', 'ieicegjjebagdjic', 'ghhjgcc', 'hjiccgcjgcace', 'gbehefggiebj', 'bdhdghjicfaadhbhjgf', 'cefdcdibdjaja', 'aegib', 'cgfiiifaeaiehijhja', 'fhfibahdhifbbag', 'ciceaghdhcaaicdfh', 'egehic', 'ccfjddhedc', 'fjhgfiicgbjbhaf', 'fhacidf', 'fdgdcbjccbdc', 'chb', 'ibbajefiajdedbg', 'dc', 'cefefafffeef', 'cjfiehfciejeihfc', 'dieaihbfeebihhfb', 'fgdfeiifi', 'dggjbihci', 'eidchjdecfe', 'fjceb', 'ibdccb', 'cfdhgifb', 'jchiccchaebdeajbjdg', 'fbgdgjcj', 'cdiechfgiabagbcgfegd', 'egceicbhddaif', 'jhbjghbg', 'aebfa', 'ihibjcehbcgdg', 'fiih', 'iiidebhaajgfegc', 'bebhgfeegahibbe', 'bbdcdggfihhihhb', 'deehhgjh', 'gdhchigfgf', 'cchicidi', 'gbddcgcfafeie', 'didaicgbfcgdbha', 'jbigcjegeghiahd', 'ja', 'ejbaijgbeedf', 'gjdghidedbijhj', 'efabghiedfgahggdhffa', 'dcfjfffebhddhdajghhe', 'jdbccjje', 'hhehcahigjafjj', 'ejbdahecgb', 'agbcjihfaafddfbbjj', 'cjjdjbceih', 'cjgcihghijebadeh', 'idfefdb', 'icfejcfdifca', 'jghdccegfiibajedcb', 'eahh', 'ijg', 'hbgcceg', 'echdgbbagagccbhjehdg', 'aahajadjchbdd', 'ghjdbfafbeeaicjija', 'ijfgijifjcbjefdidga', 'bcffbagdgecjbib', 'eegbacihcfffgcac', 'bhbhehahgg', 'gichfjieafdg', 'hjjfiecfdcicedcedg', 'edccg', 'gbb', 'ifagie', 'ffbbbbibdef', 'agfgfahicjajhbibbccb', 'jfabejcegjifdaaegcfi', 'gjajdihcigeigfieaa', 'bjgfifaaedfhabbgcjhd', 'cgeebjdfibci', 'gdijjecddhfihdcad', 'jfbajjjdebdfdjegg', 'iicegfidfaahdgg', 'eaabjfejdbfhhgga', 'ccjj', 'fecbechbjgf', 'cehbigaifjggb', 'efcfaa', 'idcjca', 'heifjaffdagihjdhhje', 'hhhg', 'bcceabajhibcgge', 'cficadfjafehcbfbe', 'ddgac', 'fgcbhchccgidhibjd', 'cfejacedhcbfbbdei', 'aadicbdgdeag', 'hbiidhd', 'jdhejfddigaig', 'dijjfhdehhgi', 'jbhbh', 'decf', 'abhdfbdjdgaigdbcdac', 'eadbghibfchhegjegaa', 'iajeahcdihdahjchejcj', 'aehbjdajff', 'efejhaihchjjjdaj', 'afaabaedac', 'jgecfabhfhacegcce', 'jbacedhij', 'jfhfeaigbehfeddgj', 'aibiebfjbbjihdafe', 'daefghfdghhdha', 'cgdgbiaijcchcdbhdg', 'fhhej', 'ihahff', 'hdiafcdg', 'bhgeigbdcjiaidfg', 'ebfcgbicei', 'jigfgfbif', 'ecfgic', 'be', 'jbfedbj', 'hfgeadbdffb', 'cdadbhfggbdcfg', 'gfbibhfid', 'dggjhibedefcidcidh', 'djgdebibbeihdb', 'idjead', 'jddfbhfiigihi', 'dahhejdh', 'aigai', 'gihjfjhbjga', 'dcdhhchgcifij', 'hbdbffehccggcahgdij', 'aicgf', 'bjdbgjjbihjfjjjei', 'cghdceieadgb', 'feeabeajdia', 'chgdgdidhac', 'bi', 'jecedadaiia', 'ifdhddbhegbhgbbhb', 'dahhdbaahgdadfdjegh', 'gbgajagegifg', 'ibeageaagibci', 'ajj', 'adabbjadgaibibadbh', 'cjgghfbfhafddahjgfdg', 'iffah', 'dcbifaaijhc', 'bd', 'ffghbj', 'afg', 'fadgedcjiedfjedaehf', 'edagghhggcbdbegeae', 'afcfibhcbbjbdeg', 'aaggi', 'aijcijjfjhb', 'jiejbjdiideibae', 'bggagfdejjaigeggagd', 'adfaecebifgdgdi', 'ejecgjhjeiiiagjchei', 'efhifgfddhhhfcdfhcai', 'djja', 'ehdfdidgahgafi', 'ejdbhd', 'ageeediidj', 'gjeachdhcibc', 'fddbaaagfacbjhch', 'ide', 'echagfgciaadhe', 'fheegadifechfad', 'ehadcaefjbifdfjjg', 'hchajigibaaei', 'didbgajbggiadeeha', 'gab', 'djjbafiai', 'dhajgdacchjefd', 'ce', 'caihabbfdcadhedigji', 'ahbgjhheijjdhjhe', 'ajaahaadcbgdaab', 'fghed', 'cijggfih', 'ifdbfegfibeeii', 'gcjbdjbbichcbjigadh', 'ibgjheegabjgdj', 'fidhdhjjedfecfbdid', 'dcbeeadg', 'ihja', 'iedhgehbgjhjfibhg', 'bdiefchcfcebff', 'ifjdddeaj', 'hbfiigihhbd', 'haifch', 'cijiee', 'agahdjjfbffhajjh', 'jehabbgihejcdbg', 'gbcibgibcbb', 'hbdiciccjbcdhgie', 'jfbdg', 'iedejciga', 'hfhcba', 'aicidjdabdaaaeb', 'ageeabaaeejdad', 'ecdb', 'egejcicbdhc', 'cfiafhjbbi', 'dfcifebiei', 'djig', 'dgbbhfedcbccafd', 'eahjbefdjgeggifdiahc', 'jbiefcfdcfdjfjef', 'if', 'jhfdhgeidei', 'jcehfafffieheajchccf', 'cgghi', 'cghfffhceihdcaihic', 'ibaiajgcbig', 'hedeaddfbahhaaccfef', 'abfecegeciggaad', 'ceiafhibhefgafjjeb', 'ggcgajfdacgbh', 'dgjj', 'abiceabf', 'dhhbhhdhhgifjacaae', 'fajchbgfbicfad', 'bagjjageadffgafhjf', 'bgcfjjeefchhjih', 'iibjigdddi', 'bda', 'fdg', 'iidjbdfded', 'cidcbjh', 'fbeibcjjddbcch', 'bgiif', 'jaijdebhffe', 'biiiegd', 'jgjjhe', 'gcdidbbfddjeabfad', 'jegibaaab', 'hiidegaa', 'hdccdcdfhcaibiajdecd', 'aihjgehhcdfacf', 'fbeggaihfcijgdjjf', 'beef', 'jjjgjjf', 'fgidffifc', 'hciacchdbggdjcgbibfe', 'fbcfjgbeddaeadhh', 'jahejfffiehijhjaedjd', 'efjggaaj', 'hcjjbjjgagjegedgf', 'ddhbhjeedcbfiejigd', 'dffddbgbefdeibdigfjf', 'feijgcj', 'bggadgiehgbhhgefd', 'addbeiggicjcbidc', 'fdjjcdheaacjgdae', 'jjbh', 'ggddgdcbagjbdbjag', 'acchhgbdfih', 'bge', 'jjfbigbgd', 'baggfhdeeaibeigjfgag', 'bjjcaihicjecahh', 'eibg', 'fffhfijeiffeafgg', 'afjeeddgciab', 'djafb', 'biegdfidfjgbecc', 'efhehhbgjg', 'ejfbjjeabjf', 'ddibajeejdbfda', 'cggdfcdijjig', 'cea']

    print(Solution().palindromePairs(words))

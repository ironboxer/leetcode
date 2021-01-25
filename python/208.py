"""
https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

"""


class TreeNode:
    def __init__(self, char, end=False):
        self.char = char
        self.end = end
        self.children = {}


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode('#')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for w in word:
            child = node.children.get(w)
            if not child:
                node.children[w] = TreeNode(w)
            node = node.children[w]
        node.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for w in prefix:
            node = node.children.get(w)
            if not node:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    # ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    # [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    tree = Trie()
    tree.insert("apple")
    print(tree.search("apple"))
    print(tree.search("app"))
    print(tree.startsWith("app"))
    tree.insert("app")
    print(tree.search("app"))

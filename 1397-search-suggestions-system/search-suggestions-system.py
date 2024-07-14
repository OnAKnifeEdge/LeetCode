class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.suggestions = []

    def insert(self, word):
        node = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def dfs_with_prefix(self, node, word):
        if len(self.suggestions) == 3:
            return
        if node.is_end:
            self.suggestions.append(word)
        for i in range(26):
            if node.children[i]:
                self.dfs_with_prefix(node.children[i], word + chr(i + ord("a")))

    def get_words_starting_with(self, prefix):
        node = self.root
        for c in prefix:
            idx = ord(c) - ord("a")
            if not node.children[idx]:
                return []
            node = node.children[idx]
        self.suggestions = []
        self.dfs_with_prefix(node, prefix)
        return self.suggestions


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)

        result = []
        prefix = ""

        for c in searchWord:
            prefix += c
            result.append(trie.get_words_starting_with(prefix))

        return result

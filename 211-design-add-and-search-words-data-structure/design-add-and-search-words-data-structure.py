class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def dfs(self, node, word, idx, path, words):
        if not node:
            return
        if idx == len(word) and node.is_end:
            words.append(path)
            return
        if idx == len(word):
            return
        c = word[idx]
        if c == '.':
            for x in node.children:
                self.dfs(node.children[x], word, idx + 1, path + x, words)
        elif c in node.children:
            self.dfs(node.children[c], word, idx + 1, path + c, words)

    def search(self, word: str) -> bool:
        words = []
        self.dfs(self.root, word, 0, '', words)
        return bool(words)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

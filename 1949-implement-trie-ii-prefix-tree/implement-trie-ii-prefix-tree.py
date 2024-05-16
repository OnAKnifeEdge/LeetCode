class TrieNode:

    def __init__(self):
        self.children = {}
        self.val = None


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        if node.val is None:
            node.val = 1
        else:
            node.val += 1

    def get_node(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def countWordsEqualTo(self, word: str) -> int:
        node = self.get_node(word)
        if node and node.val is not None:
            return node.val
        return 0


    def dfs(self, node):
        count = 0
        if node.val is not None:
            count += node.val
        for c in node.children:
            count += self.dfs(node.children[c])
        return count

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.get_node(prefix)
        return self.dfs(node) if node else 0

    def erase(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                return
            node = node.children[c]
        if node.val is None:
            return
        else:
            node.val -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)

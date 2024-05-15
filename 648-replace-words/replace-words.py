class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_shortest_key(self, key):
        node = self.root
        for idx, c in enumerate(key):
            node = node.children.get(c)
            if not node:
                break
            if node.is_end:
                return key[: idx + 1]
        return ""

    def add_key(self, key):
        node = self.root
        for c in key:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        prefix_trie = Trie()
        for key in dictionary:
            prefix_trie.add_key(key)

        words = sentence.split(" ")
        results = []
        for word in words:
            successor = prefix_trie.get_shortest_key(word)
            if not successor:
                results.append(word)
            else:
                results.append(successor)
        return " ".join(results)

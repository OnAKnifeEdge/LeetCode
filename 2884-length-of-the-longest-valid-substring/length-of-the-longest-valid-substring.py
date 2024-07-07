class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_end = True

    def has_forbidden_substring(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
            if node.is_end:
                return True
        return False


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        trie = Trie()

        for f in forbidden:
            trie.insert(f)

        n = len(word)
        right = n
        max_length = 0

        for left in range(n - 1, -1, -1):
            while left < right and trie.has_forbidden_substring(word[left:right]):
                right -= 1

            max_length = max(max_length, right - left)

        return max_length
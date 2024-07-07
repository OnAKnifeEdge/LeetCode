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

        for left in reversed(range(n)):
            # Check substrings starting from the current left position up to right
            # We only need to check substrings up to length 10 (longest forbidden length)
            for length in range(1, 11):
                if left + length > right:
                    break
                if trie.has_forbidden_substring(word[left:left + length]):
                    right = left + length - 1
                    break

            # Update the maximum length of the valid substring
            max_length = max(max_length, right - left)

        return max_length

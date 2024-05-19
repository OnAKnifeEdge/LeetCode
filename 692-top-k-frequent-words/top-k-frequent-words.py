class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            i = ord(c) - ord("a")
            if not node.children[i]:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.is_end = True

    def get_words(self, node=None, word="") -> List[str]:
        if node is None:
            node = self.root
        words = []
        if node.is_end:
            words.append(word)
        for i in range(26):
            if node.children[i]:
                words.extend(self.get_words(node.children[i], word + chr(i + ord("a"))))
        return words


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        result = []
        if k == 0:
            return result

        counter = Counter(words)
        bucket = [Trie() for _ in range(len(words) + 1)]  # n 个 bucket
        # bucket[i] is the Trie for frequency == i

        for word, frequency in counter.items():
            bucket[frequency].add(word)

        for i in reversed(range(len(words) + 1)):
            trie = bucket[i]
            result.extend(trie.get_words())
            if len(result) >= k:
                return result[:k]
        return result

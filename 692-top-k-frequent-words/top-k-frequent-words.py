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

    def get_words(self, node=None, prefix=""):
        if node is None:
            node = self.root
        words = []
        if node.is_end:
            yield prefix
        for i in range(26):
            child = node.children[i]
            if child is not None:
                yield from self.get_words(child, prefix + chr(i + ord('a')))


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
            for word in bucket[i].get_words():
                result.append(word)
                if len(result) == k:
                    return result
        return result

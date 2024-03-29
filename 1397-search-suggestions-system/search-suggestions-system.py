class TrieNode:
    def __init__(self):
        self.children = {}
        self.candidates = []

    # def __str__(self):
    #     return repr(self.children), repr(self.candidates)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.candidates.append(word)

    def add_products(self, products):
        for product in products:
            self.add_word(product)

    def search(self, word):
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return []
        return node.candidates


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        trie.add_products(products)
        suggestions = []
        for i in range(1, len(searchWord) + 1):
            word = searchWord[:i]
            suggestions.append(sorted(trie.search(word))[:3])
        return suggestions
        
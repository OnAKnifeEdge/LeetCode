class TrieNode:

    def __init__(self):
        self.val = 0
        self.children = {}


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.keys = defaultdict(int)  # additional dictionary to keep track of all keys

    def insert(self, key: str, val: int) -> None:
        node = self.root
        delta = val - self.keys[key]
        self.keys[key] = val
        for c in key:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.val += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.val



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

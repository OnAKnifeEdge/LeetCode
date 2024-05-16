class TrieNode:

    def __init__(self):
        self.val = None
        self.children = {}


class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for c in key:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.val = val

    def get_node(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def dfs(self, node):
        total = 0
        if not node:
            return None
        if node.val is not None:
            total += node.val
        for c in node.children:
            total += self.dfs(node.children[c])
        return total

    def sum(self, prefix: str) -> int:
        node = self.get_node(prefix)
        return self.dfs(node) if node else 0


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

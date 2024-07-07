class TrieNode:

    def __init__(self):
        self.content = ""
        self.is_file = False
        self.children = defaultdict(TrieNode)


class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        path = path.split("/")
        node = self.root
        # /c/d/e.file
        for p in path:
            if not p:
                continue
            node = node.children.get(p)
        if node.is_file:
            return [p]
        return sorted([i for i in node.children.keys()])

    def mkdir(self, path: str) -> None:
        self.traverse(path, False)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.traverse(filePath, False)
        node.content += content
        node.is_file = True

    def readContentFromFile(self, filePath: str) -> str:
        node = self.traverse(filePath, True)
        return node.content

    def traverse(self, path: str, read: bool) -> TrieNode:
        path = path.split("/")
        node = self.root
        for p in path:
            if not p:
                continue
            if read:
                node = node.children.get(p)
            else:
                node = node.children[p]  # create new node if non exist
        return node


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

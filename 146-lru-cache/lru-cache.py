class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
        self.size = 0
        self.cache = {}  # key: val

    def evict(self):
        if self.size <= self.capacity:
            return
        node = self.head.next
        self.remove(node)

    def remove(self, node):
        # assume node is not in cache
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.cache[node.key]
        self.size -= 1

    def add(self, node):
        # assume node is in cache
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

        self.cache[node.key] = node
        self.size += 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.add(Node(key, value))
        self.evict()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

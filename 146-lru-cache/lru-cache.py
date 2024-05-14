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
        self.d = {}  # key: val

    def get_and_make_recent(self, key):
        node = self.d[key]
        self.remove(node)
        self.add(node)
        return node.val

    def evict(self):
        node = self.head.next
        self.remove(node)

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        del self.d[node.key]
        self.size -= 1

    def add(self, node):
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node
        self.d[node.key] = node
        self.size += 1

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        return self.get_and_make_recent(key)

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        elif self.size == self.capacity:
            self.evict()

        self.add(Node(key, value))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

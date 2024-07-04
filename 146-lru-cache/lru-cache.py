class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}  # key: node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del self.cache[node.key]

    def add(self, key, val):
        node = Node(key, val)

        last_node = self.tail.prev

        last_node.next = node
        node.next = self.tail
        node.prev = last_node

        self.tail.prev = node

        self.cache[key] = node
        return node

    def evict(self):
        first_node = self.head.next
        self.remove(first_node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(key, node.val)
        return node.val

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)
            node = self.add(key, val)
            self.cache[key] = node
        else:
            if self.size == self.capacity:
                self.evict()
                self.add(key, val)

            else:
                node = self.add(key, val)
                self.cache[key] = node
                self.size += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

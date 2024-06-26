class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class FrontMiddleBackQueue:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        self.mid = None

    def pushFront(self, val: int) -> None:
        node = Node(val)
        if self.size == 0:
            self._create_first_node(node)

        elif self.size % 2 == 0:
            # even to odd: mid 不变 [1, 2] -> [3, 1, 2]
            self._push_node_to_head(node)

        else:
            #  self.size % 2 == 1:
            # odd to even: mid = mid.prev [1] -> [2, 1]
            self._push_node_to_head(node)
            self.mid = self.mid.prev

        self.size += 1

    def pushMiddle(self, val: int) -> None:
        node = Node(val)
        if self.size == 0:
            self._create_first_node(node)

        elif self.size == 1:  # mid is node
            # [1] -> [2, 1]
            self._push_node_to_head(node)
            self.mid = node
        else:
            # even to odd: mid is node. mid is not changed
            # [1, 2] -> [1, 3, 2]

            # odd to even
            # [1, 2, 3] -> [1, 4, 2, 3] mid = mid.prev
            self._push_node_to_mid(node)

        self.size += 1

    def pushBack(self, val: int) -> None:
        node = Node(val)
        if self.size == 0:
            self._create_first_node(node)
        elif self.size % 2 == 0:
            # even to odd: mid = mid.next [1, 2] -> [1, 2, 3]
            self._push_node_to_back(node)
            self.mid = self.mid.next

        else:
            # odd to even: mid 不变 [1, 2, 3] -> [1, 2, 3, 4]
            self._push_node_to_back(node)

        self.size += 1

    def popFront(self) -> int:
        if self.size == 0:
            return -1
        val = self.head.val
        if self.size == 1:
            self._create_first_node(None)

        elif self.size % 2 == 0:
            # even to odd, mid = mid.next [1, 2] -> [2]
            self._pop_node_from_head()
            self.mid = self.mid.next

        else:
            # odd to even, mid is unchanged [1, 2, 3] -> [2, 3]
            self._pop_node_from_head()

        self.size -= 1
        return val

    def popMiddle(self) -> int:
        if self.size == 0:
            return -1
        val = self.mid.val
        if self.size == 1:
            self._create_first_node(None)
        elif self.size == 2:
            # [1, 2] -> [2]
            self._pop_node_from_head()
            self.mid = self.tail
        elif self.size % 2 == 0:
            # even to odd [1, 2, 3, 4] -> [1, 3, 4] mid = mid.next
            self._pop_node_from_middle()
            self.mid = self.mid.next
        else:
            # odd to even [1, 2, 3] -> [1, 3] mid = mid.prev
            self._pop_node_from_middle()
            self.mid = self.mid.prev

        self.size -= 1
        return val

    def popBack(self) -> int:
        if self.size == 0:
            return -1
        val = self.tail.val
        if self.size == 1:
            self._create_first_node(None)
        elif self.size % 2 == 0:
            # even to odd: [1, 2, 3, 4] -> [1, 2, 3] mid unchanged
            self._pop_node_from_tail()
        else:
            # odd to even: [1, 2, 3] -> [1, 2] mid = mid.prev
            self._pop_node_from_tail()
            self.mid = self.mid.prev

        self.size -= 1
        return val

    def _create_first_node(self, node):
        self.head = self.mid = self.tail = node

    def _push_node_to_head(self, node):
        node.next = self.head
        self.head.prev = node
        self.head = node

    def _push_node_to_back(self, node):
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def _push_node_to_mid(self, node):
        # even to odd: mid is node. mid is not changed
        # [1, 2] -> [1, 3, 2]

        # odd to even
        # [1, 2, 3] -> [1, 4, 2, 3] mid = mid.prev

        if self.size % 2 == 1:
            # mid 前 insert:
            prev = self.mid.prev
            nxt = self.mid

            prev.next = node
            node.prev = prev

            node.next = nxt
            nxt.prev = node
            self.mid = node
        else:
            # mid 后 insert
            prev = self.mid
            nxt = self.mid.next

            prev.next = node
            node.prev = prev

            node.next = nxt
            nxt.prev = node

            self.mid = node

    def _pop_node_from_head(self):
        nxt = self.head.next
        self.head = nxt
        self.head.prev = None

    def _pop_node_from_tail(self):
        prev = self.tail.prev
        self.tail = prev
        self.tail.next = None

    def _pop_node_from_middle(self):
        prev = self.mid.prev
        nxt = self.mid.next
        prev.next = nxt
        nxt.prev = prev


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

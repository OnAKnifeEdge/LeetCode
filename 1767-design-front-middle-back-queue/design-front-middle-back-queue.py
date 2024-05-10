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

    def create_first_node(self, node):
        self.head = self.mid = self.tail = node

    def push_node_to_head(self, node):
        node.next = self.head
        self.head.prev = node
        self.head = node

    def push_node_to_back(self, node):
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def push_node_to_mid(self, node):
        nxt = self.mid.next
        curr = self.mid

        curr.next = node
        node.prev = curr

        node.next = nxt
        nxt.prev = node

        self.mid = node

    def pushFront(self, val: int) -> None:
        node = Node(val)
        if self.size == 0:
            self.create_first_node(node)

        elif self.size % 2 == 0:
            # even to odd: mid 不变 [1, 2] -> [3, 1, 2]
            self.push_node_to_head(node)

        else:
            #  self.size % 2 == 1:
            # odd to even: mid = mid.prev [1] -> [2, 1]
            self.push_node_to_head(node)
            self.mid = self.mid.prev

        self.size += 1

    def pushMiddle(self, val: int) -> None:
        node = Node(val)
        if self.size == 0:
            self.create_first_node(node)

        elif self.size == 1:  # mid is node
            # [1] -> [2, 1]
            node.next = self.tail
            self.tail.prev = node
            self.head = node
            self.mid = node

        elif self.size % 2 == 0:
            # even to odd: mid is node. mid is not changed
            # [1, 2] -> [1, 3, 2]
            self.push_node_to_mid(node)

        else:
            # odd to even
            # [1, 2, 3] -> [1, 4, 2, 3] mid = mid.prev
            self.mid = self.mid.prev
            self.push_node_to_mid(node)

        self.size += 1

    def pushBack(self, val: int) -> None:
        node = Node(val)
        if self.size == 0:
            self.create_first_node(node)
        elif self.size % 2 == 0:
            # even to odd: mid = mid.next [1, 2] -> [1, 2, 3]
            self.push_node_to_back(node)
            self.mid = self.mid.next

        else:
            # odd to even: mid 不变 [1, 2, 3] -> [1, 2, 3, 4]
            self.push_node_to_back(node)

        self.size += 1

    def pop_node_from_head(self):
        nxt = self.head.next
        self.head = nxt
        self.head.prev = None

    def popFront(self) -> int:
        if self.size == 0:
            return -1
        val = self.head.val
        if self.size == 1:
            self.create_first_node(None)

        elif self.size % 2 == 0:
            # even to odd, mid = mid.next [1, 2] -> [2]
            self.pop_node_from_head()
            self.mid = self.mid.next

        else:
            self.pop_node_from_head()
            # odd to even, mid is unchanged [1, 2, 3] -> [2, 3]

        # elif self.size % 2 == 1:
        #     self.head = self.head.next
        #     self.head.prev = None
        # else:
        #     self.head = self.head.next
        #     self.head.prev = None
        #     self.mid = self.mid.next

        self.size -= 1
        return val

    def popMiddle(self) -> int:
        if self.size == 0:
            return -1
        ret = self.mid.val
        if self.size == 1:
            self.head = self.mid = self.tail = None
        elif self.size == 2:
            self.head = self.mid = self.tail
            self.head.prev = None
        elif self.size % 2 == 1:
            n = self.mid.next
            self.mid = self.mid.prev
            self.mid.next = n
            n.prev = self.mid
        else:
            p = self.mid.prev
            n = self.mid.next
            p.next = n
            n.prev = p
            self.mid = n
        self.size -= 1
        # print('popmiddle',self.head.val if self.head else None,self.mid.val if self.mid else None,self.tail.val if self.tail else None,self.size)
        return ret

    def popBack(self) -> int:
        if self.size == 0:
            return -1
        ret = self.tail.val
        if self.size == 1:
            self.head = self.mid = self.tail = None
        elif self.size == 2:
            self.tail = self.head
            self.head.next = None
        elif self.size % 2 == 1:
            self.mid = self.mid.prev
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        # print('popback',self.head.val if self.head else None,self.mid.val if self.mid else None,self.tail.val if self.tail else None,self.size)
        return ret


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

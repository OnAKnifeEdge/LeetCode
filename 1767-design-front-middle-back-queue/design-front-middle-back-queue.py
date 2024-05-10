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

    def pushFront(self, val: int) -> None:
        node = Node(val)
        if self.size == 0:
            self.create_first_node(node)

        elif self.size == 1:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.mid = node

        elif self.size == 2:  # mid 不变
            node.next = self.head
            self.head.prev = node
            # self.mid = self.head  # can i remove it since mid is not changed
            self.head = node

        elif self.size % 2 == 1:  # mid 变前一个
            node.next = self.head
            self.head.prev = node
            self.mid = self.mid.prev
            self.head = node

        else:  # mid 不变
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.size += 1

    def pushMiddle(self, val: int) -> None:
        newNode = Node(val)
        if self.size == 0:
            self.head = self.mid = self.tail = newNode
        elif self.size == 1:
            self.head = self.mid = newNode
            self.head.next = self.tail
            self.tail.prev = self.head
        elif self.size == 2:
            self.mid = newNode
            self.mid.next = self.tail
            self.mid.prev = self.head
            self.head.next = self.mid
            self.tail.prev = self.mid
        elif self.size % 2 == 1:
            prev = self.mid.prev
            next = self.mid
            self.mid = newNode
            self.mid.next = next
            self.mid.prev = prev
            prev.next = self.mid
            next.prev = self.mid
        else:
            p = self.mid
            n = self.mid.next
            self.mid = newNode
            self.mid.next = n
            self.mid.prev = p
            p.next = self.mid
            n.prev = self.mid
        self.size += 1
        # print('pushmiddle',self.head.val if self.head else None,self.mid.val if self.mid else None,self.tail.val if self.tail else None,self.size)

    def pushBack(self, val: int) -> None:
        newNode = Node(val)
        if self.size == 0:
            self.head = self.mid = self.tail = newNode
        elif self.size == 1:
            self.tail = newNode
            self.tail.prev = self.head
            self.head.next = self.tail
        elif self.size == 2:
            self.tail = newNode
            self.mid = self.head.next
            self.mid.next = self.tail
            self.tail.prev = self.mid
        elif self.size % 2 == 1:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.mid = self.mid.next
        self.size += 1
        # print('pushback',self.head.val if self.head else None,self.mid.val if self.mid else None,self.tail.val if self.tail else None,self.size)

    def popFront(self) -> int:
        if self.size == 0:
            return -1
        ret = self.head.val
        if self.size == 1:
            self.head = self.mid = self.tail = None
        elif self.size == 2:
            self.head = self.mid = self.tail
            self.head.prev = None
        elif self.size % 2 == 1:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = self.head.next
            self.head.prev = None
            self.mid = self.mid.next
        self.size -= 1
        # print('popfront',self.head.val if self.head else None,self.mid.val if self.mid else None,self.tail.val if self.tail else None,self.size)
        return ret

    def pushMiddle(self, val: int) -> None:
        newNode = Node(val)
        if self.size == 0:
            self.head = self.mid = self.tail = newNode
        elif self.size == 1:
            self.head = self.mid = newNode
            self.head.next = self.tail
            self.tail.prev = self.head
        elif self.size == 2:
            self.mid = newNode
            self.mid.next = self.tail
            self.mid.prev = self.head
            self.head.next = self.mid
            self.tail.prev = self.mid
        elif self.size % 2 == 1:
            prev = self.mid.prev
            next = self.mid
            self.mid = newNode
            self.mid.next = next
            self.mid.prev = prev
            prev.next = self.mid
            next.prev = self.mid
        else:
            p = self.mid
            n = self.mid.next
            self.mid = newNode
            self.mid.next = n
            self.mid.prev = p
            p.next = self.mid
            n.prev = self.mid
        self.size += 1
        # print('pushmiddle',self.head.val if self.head else None,self.mid.val if self.mid else None,self.tail.val if self.tail else None,self.size)

    def pushBack(self, val: int) -> None:
        newNode = Node(val)
        if self.size == 0:
            self.head = self.mid = self.tail = newNode
        elif self.size == 1:
            self.tail = newNode
            self.tail.prev = self.head
            self.head.next = self.tail
        elif self.size == 2:
            self.tail = newNode
            self.mid = self.head.next
            self.mid.next = self.tail
            self.tail.prev = self.mid
        elif self.size % 2 == 1:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.mid = self.mid.next
        self.size += 1
        # print('pushback',self.head.val if self.head else None,self.mid.val if self.mid else None,self.tail.val if self.tail else None,self.size)

    def popFront(self) -> int:
        if self.size == 0:
            return -1
        ret = self.head.val
        if self.size == 1:
            self.head = self.mid = self.tail = None
        elif self.size == 2:
            self.head = self.mid = self.tail
            self.head.prev = None
        elif self.size % 2 == 1:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = self.head.next
            self.head.prev = None
            self.mid = self.mid.next
        self.size -= 1
        # print('popfront',self.head.val if self.head else None,self.mid.val if self.mid else None,self.tail.val if self.tail else None,self.size)
        return ret

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

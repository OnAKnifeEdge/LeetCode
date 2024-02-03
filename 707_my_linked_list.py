from typing import Optional


class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:

        # if index is invalid
        if index < 0 or index >= self.size:
            return -1

        pre = self.find_index_pre(index)
        return pre.next.val

        # pre = self.head
        # # possible optimization decide which end is faster
        # for _ in range(index + 1):
        #     pre = pre.next
        # return pre.val

    def addAtHead(self, val: int) -> None:
        # head (prev) - |node| 1 (nxt) - 2 - 3 -tail
        self.size += 1
        node = ListNode(val)
        pre, nxt = self.head, self.head.next
        node.prev = pre
        node.next = nxt
        pre.next = node
        nxt.pre = node

    def addAtTail(self, val: int) -> None:
        # head - 1 - 2 - 3(prev) - |node| tail (nxt)
        self.size += 1
        node = ListNode(val)
        nxt, pre = self.tail, self.tail.prev
        node.prev = pre
        node.next = nxt
        pre.next = node
        nxt.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        # head - 1 (pre) - (node index = 0) - 2 (nxt)- 3 - tail
        if index < 0 or index > self.size:
            return
        # pre = self.head
        # # possible optimization decide which end is faster
        # for _ in range(index):
        #     pre = pre.next

        pre = self.find_index_pre(index)
        nxt = pre.next

        self.size += 1
        node = ListNode(val)
        node.next = nxt
        node.prev = pre
        pre.next = node
        nxt.prev = node

    def deleteAtIndex(self, index: int) -> None:

        # head - 1 (pre) - 2 - 3 (nxt) - tail (index = 1 remove val = 2)
        if index < 0 or index >= self.size:
            return

        self.size -= 1
        # pre = self.head
        # # possible optimization decide which end is faster
        # for _ in range(index):
        #     pre = pre.next

        pre = self.find_index_pre(index)
        nxt = pre.next.next

        pre.next = nxt
        nxt.prev = pre

    def find_index_pre(self, index: int) -> Optional[ListNode]:
        if index < 0 or index >= self.size:
            return None

        pre = self.head
        for _ in range(index):
            pre = pre.next
        return pre


# Your MyLinkedList object will be instantiated and called as such:
l = MyLinkedList()
print(l.size)
# l.addAtTail(4)
# print(l.get(0))
l.addAtHead(1)
print(l.get(0))
l.addAtTail(3)
# l.addAtTail(4)
print(l.get(1))
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

class MinHeap:
    """Implement min heap structure from scratch in Python"""

    def __init__(self):
        """Initialize an empty heap"""
        self.heap = []

    def push(self, val: int):
        """Add a value to the heap, maintaining the min heap property"""
        self.heap.append(val)
        self.bubble_up(len(self.heap) - 1)


    def pop(self):
        """Remove and return the smallest element in the heap"""
        if not self.heap:
            return None
        # put the smallest to the end and pop
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        val = self.heap.pop()
        self.bubble_down(0)
        return val

    def bubble_up(self, idx):
        """Bubbles up the value at given index to its correct place in the heap to maintain heap property"""
        if idx <= 0:
            return
        parent_idx = (idx - 1) // 2
        if self.heap[idx] >= self.heap[parent_idx]:
            return
        self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
        self.bubble_up(parent_idx)

    def bubble_down(self, idx):
        """Bubbles down the value at the index to its correct place in the heap to maintain heap property"""
        left_idx, right_idx = 2 * idx + 1, 2 * idx + 2
        smallest_idx = idx
        if left_idx < len(self.heap) and self.heap[smallest_idx] > self.heap[left_idx]:
            smallest_idx = left_idx
        if right_idx < len(self.heap) and self.heap[smallest_idx] > self.heap[right_idx]:
            smallest_idx = right_idx
        if smallest_idx != idx:
            self.heap[smallest_idx], self.heap[idx] = self.heap[idx], self.heap[smallest_idx]
            self.bubble_down(smallest_idx)


    def peek(self):
        """Returns the smallest value from the heap without removing it"""
        return self.heap[0] if self.heap else None
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/solutions/2683563/python3-xor-solution/
        path = deque()
        level = 0

        while 1 << level <= label:
            level += 1

        while label > 0:
            path.appendleft(label)
            min_val = 1 << (level - 1)
            max_val = (1 << level) - 1
            label = min_val + max_val - label
            label //= 2
            level -= 1

        return list(path)

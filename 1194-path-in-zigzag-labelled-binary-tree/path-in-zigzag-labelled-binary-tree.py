class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        x = label
        mask = 0

        # Step 1: Build the mask for the given level
        while x > 1:
            x >>= 1
            mask = (mask << 1) | 1  # Expanding mask by shifting left and adding 1

        x = label
        result = []

        # Step 2: Traverse up the tree while flipping labels at each level
        while x:
            result.append(x)
            # Store current label at the front (since we go bottom-up)
            x >>= 1  # Move to parent
            mask >>= 1  # Reduce the mask for the next level
            x ^= mask  # Flip the label in the zigzag order

        return result[::-1]

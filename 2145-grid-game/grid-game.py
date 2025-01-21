class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        first_row_sum = sum(grid[0])
        second_row_sum = 0
        minimal_sum = float('inf')
        for turn_index in range(len(grid[0])):
            first_row_sum -= grid[0][turn_index]
            minimal_sum = min(minimal_sum, max(first_row_sum, second_row_sum))
            second_row_sum += grid[1][turn_index]
        return minimal_sum
        
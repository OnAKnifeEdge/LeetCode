from typing import List


# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

class Solution:

    def is_valid(self, numbers: List[str]):
        for num in numbers:
            if num.isdigit() and (int(num) < 1 or int(num) > 9):
                return False
            elif num == '.':
                continue
            else:
                return False
        return len(set(numbers)) == len(numbers)

    def is_row_valid(self, board: List[List[str]]):
        for row in board:
            if not self.is_valid(row):
                return False
        return True

    def is_column_valid(self, board: List[List[str]]):
        for col in zip(*board):
            if not self.is_valid(col):
                return False
        return True

    def is_square_valid(self, board: List[List[str]]):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                flat_list = [item for sublist in square for item in sublist]
                if not self.is_valid(flat_list):
                    return False
        return True

    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        return self.is_row_valid(board) and self.is_column_valid(board) and self.is_square_valid(board)

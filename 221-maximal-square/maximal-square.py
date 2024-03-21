class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Get the dimensions of the matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # Initialize the dp array
        dp = [[0] * COLS for _ in range(ROWS)]
        
        # Initialize the max size of the square seen so far
        max_size = 0
        
        # Fill the dp array
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == '0':
                    continue

                if i == 0 or j == 0:
                    # First row or column, so the maximum size of the square is 1
                    dp[i][j] = 1
                else:
                    # Check the values of the cells to the left, top, and top-left of the current cell
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                # Update the max size of the square seen so far
                max_size = max(max_size, dp[i][j])
        
        # Return the area of the largest square
        return max_size ** 2
        
#         ROWS, COLS = len(matrix), len(matrix[0])
#         cache = {} # map each (r, c) -> maxLength of square
        
#         def dp(r, c):
#             if r >= ROWS or c >= COLS:
#                 return 0
            
#             if (r, c) not in cache:
#                 down = dp(r + 1, c)
#                 right = dp(r, c + 1)
#                 diag = dp(r + 1, c + 1)
                
#                 cache[(r, c)] = 0
#                 if matrix[r][c] == '1':
#                     cache[(r, c)] = 1 + min(down, right, diag)
                    
                
            
#             return cache[(r, c)]
        
#         dp(0, 0)
#         return max(cache.values()) ** 2


        
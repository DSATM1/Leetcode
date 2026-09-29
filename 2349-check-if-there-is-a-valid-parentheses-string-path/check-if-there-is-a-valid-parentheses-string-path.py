class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # A valid parentheses string must have an even length.
        # The path length from (0,0) to (m-1, n-1) is exactly m + n - 1.
        if (m + n - 1) % 2 != 0:
            return False
            
        # A valid path must start with an open parenthesis and end with a closed one.
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        from functools import lru_cache
        
        @lru_cache(None)
        def dfs(r, c, balance):
            # Out of bounds
            if r >= m or c >= n:
                return False
                
            # Update the balance (open brackets minus close brackets)
            balance += 1 if grid[r][c] == '(' else -1
            
            # If there are more closing brackets than opening brackets at any point, it's invalid
            if balance < 0:
                return False
                
            # If we reached the destination, check if the balance is exactly 0
            if r == m - 1 and c == n - 1:
                return balance == 0
                
            # Move down or right
            return dfs(r + 1, c, balance) or dfs(r, c + 1, balance)
            
        return dfs(0, 0, 0)
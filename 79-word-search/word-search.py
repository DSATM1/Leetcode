class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, i):
            # If we've matched all characters, the word is found
            if i == len(word):
                return True
            
            # Check boundaries and if the current character matches
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                board[r][c] != word[i]):
                return False
            
            # Temporarily mark the cell as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all 4 adjacent directions
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            # Backtrack and restore the original character
            board[r][c] = temp
            
            return res

        # Iterate through every cell on the board to find a starting point
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                    
        return False
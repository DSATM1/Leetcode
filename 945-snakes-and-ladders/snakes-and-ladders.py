from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        
        # Helper function to convert square number to (row, col)
        def get_coordinates(square):
            r = n - 1 - (square - 1) // n
            c = (square - 1) % n
            # If the row from the bottom is odd, the columns go right to left
            if (n - 1 - r) % 2 != 0:
                c = n - 1 - c
            return r, c
            
        # Queue stores (current_square, number_of_rolls)
        queue = deque([(1, 0)])
        visited = {1}
        
        while queue:
            curr, rolls = queue.popleft()
            
            # If we reach the last square, return the roll count
            if curr == n * n:
                return rolls
                
            # Try all possible dice rolls (1 to 6)
            for i in range(1, 7):
                next_square = curr + i
                if next_square > n * n:
                    break
                    
                r, c = get_coordinates(next_square)
                
                # If there's a snake or ladder, take it
                if board[r][c] != -1:
                    destination = board[r][c]
                else:
                    destination = next_square
                    
                # If we haven't visited this destination, add it to the queue
                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, rolls + 1))
                    
        # If the queue empties and we never reached the end
        return -1
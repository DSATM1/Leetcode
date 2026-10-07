class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Helper function to check if a string has valid parentheses
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                
                # More closing than opening parentheses
                if count < 0:
                    return False
            return count == 0
        
        # Start the BFS with the original string in our current "level"
        level = {s}
        
        while True:
            # Filter the current level for only valid strings
            valid = list(filter(is_valid, level))
            
            # If we found valid strings, return them (guarantees minimum removals)
            if valid:
                return valid
            
            # Otherwise, generate the next level by removing one parenthesis 
            # from each string in the current level
            level = {
                curr[:i] + curr[i+1:] 
                for curr in level 
                for i in range(len(curr)) 
                if curr[i] in '()'
            }
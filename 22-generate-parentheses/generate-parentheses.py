class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_string, open_count, close_count):
            # Base case: If the string length is 2 * n, we've used all parentheses
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # If we haven't used all open parentheses, we can add one
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
            
            # We can only add a close parenthesis if it pairs with an unmatched open one
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
                
        # Start the recursion with an empty string and 0 counts
        backtrack("", 0, 0)
        
        return result
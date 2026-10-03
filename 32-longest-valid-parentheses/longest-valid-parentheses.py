class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        # Initialize stack with -1 to serve as the base index for valid substrings
        stack = [-1]
        
        for i, char in enumerate(s):
            if char == '(':
                # Push the index of the open parenthesis
                stack.append(i)
            else:
                # Pop the last open parenthesis index
                stack.pop()
                
                if not stack:
                    # If stack is empty, this closing parenthesis is unmatched.
                    # Push its index to serve as the new base for future valid substrings.
                    stack.append(i)
                else:
                    # Calculate the length of the current valid substring
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len
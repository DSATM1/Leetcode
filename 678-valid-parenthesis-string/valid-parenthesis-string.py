class Solution:
    def checkValidString(self, s: str) -> bool:
        # cmin tracks the minimum possible number of open parentheses
        # cmax tracks the maximum possible number of open parentheses
        cmin = 0
        cmax = 0
        
        for char in s:
            if char == '(':
                cmax += 1
                cmin += 1
            elif char == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            elif char == '*':
                cmax += 1  # if '*' is treated as '('
                cmin = max(cmin - 1, 0)  # if '*' is treated as ')' or empty
            
            # If cmax is negative, it means we have too many ')' that can't be balanced
            if cmax < 0:
                return False
                
        # The string is valid if the minimum possible open parentheses is 0
        return cmin == 0
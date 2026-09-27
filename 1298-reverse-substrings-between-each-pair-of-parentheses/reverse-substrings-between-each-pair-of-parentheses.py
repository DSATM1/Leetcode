class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [0] * n
        stack = []
        
        # Pass 1: Find matching pairs of parentheses
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                j = stack.pop()
                pair[i], pair[j] = j, i
                
        # Pass 2: Traverse and build the string
        res = []
        i, d = 0, 1
        
        while i < n:
            if s[i] == '(' or s[i] == ')':
                # Teleport to the matching parenthesis and reverse direction
                i = pair[i]
                d = -d
            else:
                res.append(s[i])
            i += d
            
        return "".join(res)
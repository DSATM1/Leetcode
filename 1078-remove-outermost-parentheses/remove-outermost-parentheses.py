class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        opened = 0
        
        for char in s:
            if char == '(':
                # If 'opened' is greater than 0, this is not the outermost '('
                if opened > 0:
                    res.append(char)
                opened += 1
            else:
                opened -= 1
                # If 'opened' is greater than 0, this is not the outermost ')'
                if opened > 0:
                    res.append(char)
                    
        return "".join(res)
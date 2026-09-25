class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def dfs(exp):
            # Find the first closing brace
            right = exp.find('}')
            
            # Base case: if there are no braces, it's a fully resolved word
            if right == -1:
                return {exp}
            
            # Find the closest matching opening brace to get the innermost block
            left = exp.rfind('{', 0, right)
            
            # Extract the comma-separated options inside these braces
            parts = exp[left+1:right].split(',')
            
            # Recursively resolve the rest of the string for each option
            res = set()
            for part in parts:
                # Substitute the '{...}' block with the current option and recurse
                res.update(dfs(exp[:left] + part + exp[right+1:]))
            
            return res
        
        # The problem requires a sorted list of unique words
        return sorted(list(dfs(expression)))
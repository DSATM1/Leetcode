class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        needed_right = 0
        
        for char in s:
            if char == '(':
                # If we have an odd number of needed right parentheses, it means we 
                # have a single ')' waiting for another ')'. Since we just found a '(', 
                # we must insert a ')' right here to complete the '))' pair.
                if needed_right % 2 != 0:
                    insertions += 1
                    needed_right -= 1
                
                # Each '(' needs two ')'
                needed_right += 2
                
            else: # char == ')'
                needed_right -= 1
                
                # If needed_right is negative, we have a closing ')' without an opening '('
                if needed_right < 0:
                    insertions += 1 # Insert one '('
                    needed_right += 2 # The new '(' needs two ')', minus the one we just processed = 1
                    
        # Add any remaining right parentheses that are still needed at the end
        return insertions + needed_right
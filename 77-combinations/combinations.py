from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, current_combination):
            # Base case: if the combination is of length k, add a copy of it to the result
            if len(current_combination) == k:
                result.append(current_combination[:])
                return
            
            # Explore all possible numbers from 'start' to 'n'
            # (Optimization: We can stop early if there aren't enough numbers left to reach length k)
            for i in range(start, n + 1 - (k - len(current_combination)) + 1):
                current_combination.append(i)
                backtrack(i + 1, current_combination)
                current_combination.pop() # Backtrack: remove the last element to try the next one
                
        backtrack(1, [])
        return result
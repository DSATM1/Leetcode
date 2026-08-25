import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            # Calculate total hours needed at speed mid
            hours_needed = sum((pile + mid - 1) // mid for pile in piles)
            
            if hours_needed <= h:
                ans = mid       # mid is a valid speed, try searching for smaller
                high = mid - 1
            else:
                low = mid + 1   # speed mid is too slow, increase speed
                
        return ans
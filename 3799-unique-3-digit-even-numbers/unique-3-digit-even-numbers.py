from collections import Counter
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        available = Counter(digits)
        valid_count = 0
        
        # Check all possible 3-digit even numbers
        for num in range(100, 1000, 2):
            required = Counter(int(d) for d in str(num))
            
            # If our digits array has enough of each needed digit, it's a valid match
            if all(available[d] >= count for d, count in required.items()):
                valid_count += 1
                
        return valid_count
import collections
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        
        reserved = collections.defaultdict(set)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                reserved[row].add(seat)
        
        
        max_families = (n - len(reserved)) * 2
        
        
        for seats in reserved.values():
            
            left_free = not bool(seats & {2, 3, 4, 5})
            right_free = not bool(seats & {6, 7, 8, 9})
            mid_free = not bool(seats & {4, 5, 6, 7})
            
            if left_free and right_free:
                max_families += 2

            elif left_free or right_free or mid_free:
                max_families += 1
                
        return max_families
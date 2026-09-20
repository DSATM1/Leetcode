class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # Calculate the absolute difference between 'L' and 'R' moves
        fixed_distance = abs(moves.count('L') - moves.count('R'))
        
        # All '_' can be used to move further in the direction of the majority
        return fixed_distance + moves.count('_')
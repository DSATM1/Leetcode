class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # If the strings are not the same length, they cannot be rotations
        if len(s) != len(goal):
            return False
            
        # All possible rotations of 's' are contained within 's + s'
        return goal in (s + s)
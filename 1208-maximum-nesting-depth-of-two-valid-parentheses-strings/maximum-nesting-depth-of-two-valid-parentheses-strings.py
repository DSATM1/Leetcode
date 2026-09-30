class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0
        for char in seq:
            if char == '(':
                # Assign opening parenthesis based on current depth
                ans.append(depth % 2)
                depth += 1
            else:
                # Decrement depth first, then assign closing parenthesis to match its pair
                depth -= 1
                ans.append(depth % 2)
        return ans
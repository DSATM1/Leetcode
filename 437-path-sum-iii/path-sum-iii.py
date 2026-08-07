# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Base case: a path starting from root itself
        
        def dfs(node: Optional[TreeNode], curr_sum: int) -> int:
            if not node:
                return 0
            
            # Update running sum for current path
            curr_sum += node.val
            
            # Count valid paths ending at this node
            count = prefix_sums[curr_sum - targetSum]
            
            # Record current path sum frequency
            prefix_sums[curr_sum] += 1
            
            # Recurse on child nodes
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            # Backtrack: remove current sum so it doesn't affect other branches
            prefix_sums[curr_sum] -= 1
            
            return count
        
        return dfs(root, 0)
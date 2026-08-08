# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0
        
        def dfs(node, go_left, go_right):
            if not node:
                return
            
            # Update the global maximum length seen so far
            self.max_len = max(self.max_len, go_left, go_right)
            
            # Move to left child:
            # - Continues path from right (go_right + 1)
            # - Resets path from left to 1
            dfs(node.left, go_right + 1, 0)
            
            # Move to right child:
            # - Continues path from left (go_left + 1)
            # - Resets path from right to 1
            dfs(node.right, 0, go_left + 1)
            
        # Start DFS with initial path lengths of 0 for root
        dfs(root, 0, 0)
        return self.max_len
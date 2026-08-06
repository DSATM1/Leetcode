# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_so_far: int) -> int:
            if not node:
                return 0
            
            # Check if the current node is a "good" node
            is_good = 1 if node.val >= max_so_far else 0
            
            # Update the maximum value seen so far for child nodes
            new_max = max(max_so_far, node.val)
            
            # Traverse left and right subtrees
            return is_good + dfs(node.left, new_max) + dfs(node.right, new_max)

        # Start DFS with the root's value as the initial maximum
        return dfs(root, root.val)
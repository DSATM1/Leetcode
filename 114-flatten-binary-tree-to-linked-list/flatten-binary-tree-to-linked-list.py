# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        
        while curr:
            if curr.left:
                # Find the rightmost node of the left subtree
                runner = curr.left
                while runner.right:
                    runner = runner.right
                
                # Attach the current right subtree to the rightmost node
                runner.right = curr.right
                
                # Move the left subtree to the right and nullify the left pointer
                curr.right = curr.left
                curr.left = None
                
            # Move on to the right node to continue the process
            curr = curr.right
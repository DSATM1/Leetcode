# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        
        def isMirror(t1, t2):
            # If both nodes are null, they are symmetric
            if not t1 and not t2:
                return True
            # If only one is null, they are not symmetric
            if not t1 or not t2:
                return False
            # Check if current values match and their subtrees are mirrors
            return (t1.val == t2.val) and \
                   isMirror(t1.right, t2.left) and \
                   isMirror(t1.left, t2.right)
        
        return isMirror(root.left, root.right)
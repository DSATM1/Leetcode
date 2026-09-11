class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are null, the trees are identical at this level
        if not p and not q:
            return True
        
        # If only one node is null, or their values are different, they are not identical
        if not p or not q or p.val != q.val:
            return False
            
        # Recursively check if both left and right subtrees are identical
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
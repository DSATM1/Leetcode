class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # If the tree is empty, there is no path
        if not root:
            return False
        
        # If it's a leaf node, check if its value equals the remaining target sum
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursively check the left and right subtrees with the updated target sum
        remaining_sum = targetSum - root.val
        return (self.hasPathSum(root.left, remaining_sum) or 
                self.hasPathSum(root.right, remaining_sum))
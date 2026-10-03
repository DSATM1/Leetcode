class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def depth(node):
            if not node:
                return 0
            
            # Recursively find the depth of the left and right subtrees
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # The diameter passing through the current node is the sum of left and right depths
            # Update the global maximum if this path is longer
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            
            # Return the depth of the tree rooted at the current node
            return 1 + max(left_depth, right_depth)
        
        depth(root)
        return self.max_diameter
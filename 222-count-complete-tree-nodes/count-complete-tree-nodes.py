class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def get_depth(node, go_left):
            depth = 0
            while node:
                depth += 1
                node = node.left if go_left else node.right
            return depth
        
        left_depth = get_depth(root, True)
        right_depth = get_depth(root, False)
        
        # If left and right depths are equal, it's a perfect binary tree.
        # The number of nodes is 2^h - 1
        if left_depth == right_depth:
            return (1 << left_depth) - 1
            
        # Otherwise, recursively count the nodes in the left and right subtrees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
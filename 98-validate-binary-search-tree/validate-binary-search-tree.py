class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            # An empty tree is a valid BST
            if not node:
                return True
            
            # The current node's value must be between low and high
            if node.val <= low or node.val >= high:
                return False
            
            # Recursively validate the left and right subtrees
            # Left subtree elements must be strictly less than node.val
            # Right subtree elements must be strictly greater than node.val
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        return validate(root)
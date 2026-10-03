class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        
        while curr or stack:
            # Reach the left most Node of the current Node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Current must be None at this point
            curr = stack.pop()
            result.append(curr.val)
            
            # We have visited the node and its left subtree. Now, it's right subtree's turn
            curr = curr.right
            
        return result
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # Create a hash map to instantly find the index of any root value in the inorder list
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Turn preorder into an iterator so we can sequentially grab the next root
        preorder_iter = iter(preorder)
        
        def build(left, right):
            # Base case: if there are no elements to construct the tree
            if left > right:
                return None
            
            # The first element in current preorder is always the root of the current subtree
            root_val = next(preorder_iter)
            root = TreeNode(root_val)
            
            # Find the root's position in the inorder traversal
            mid = inorder_map[root_val]
            
            # Recursively build the left and right subtrees. 
            # Note: Left must be built first because preorder is (root -> left -> right)
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, len(inorder) - 1)
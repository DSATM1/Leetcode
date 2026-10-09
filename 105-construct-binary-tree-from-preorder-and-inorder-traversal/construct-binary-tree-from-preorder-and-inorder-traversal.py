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
        
        # Iterator to fetch the next root value from preorder in O(1)
        preorder_iter = iter(preorder)
        
        def array_to_tree(left: int, right: int) -> TreeNode | None:
            # Base case: if there are no elements to construct the tree
            if left > right:
                return None
            
            # The next element in preorder is always the root of the current subtree
            root_val = next(preorder_iter)
            root = TreeNode(root_val)
            
            # Get the index of this root in the inorder traversal
            mid = inorder_map[root_val]
            
            # Recursively build the left and right subtrees
            # Note: We must build the left subtree first because the preorder 
            # iterator progresses in a Root -> Left -> Right pattern.
            root.left = array_to_tree(left, mid - 1)
            root.right = array_to_tree(mid + 1, right)
            
            return root
            
        return array_to_tree(0, len(inorder) - 1)
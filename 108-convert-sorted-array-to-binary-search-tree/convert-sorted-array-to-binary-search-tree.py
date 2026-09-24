class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def helper(left, right):
            if left > right:
                return None
            
            # Always choose the middle element to ensure height balance
            mid = (left + right) // 2
            
            # Create the root node
            root = TreeNode(nums[mid])
            
            # Recursively build the left and right subtrees
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
        
        return helper(0, len(nums) - 1)
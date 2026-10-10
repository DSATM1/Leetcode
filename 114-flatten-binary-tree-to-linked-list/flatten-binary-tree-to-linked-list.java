class Solution {
    public void flatten(TreeNode root) {
        TreeNode curr = root;
        
        while (curr != null) {
            // If there's a left child, we need to wire it into the right path
            if (curr.left != null) {
                // Find the rightmost node of the left subtree
                TreeNode runner = curr.left;
                while (runner.right != null) {
                    runner = runner.right;
                }
                
                // Rewire the connections
                runner.right = curr.right;
                curr.right = curr.left;
                curr.left = null;
            }
            
            // Move on to the next node on the right
            curr = curr.right;
        }
    }
}
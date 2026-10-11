class Solution {
    public int sumOfSquares(int[] nums) {
        int n = nums.length;
        int sum = 0;
        
        // Iterate from 1 to n since the problem uses 1-based indexing
        for (int i = 1; i <= n; i++) {
            // Check if i is a special index
            if (n % i == 0) {
                // Add the square of the element (adjusting for 0-based array index)
                sum += nums[i - 1] * nums[i - 1];
            }
        }
        
        return sum;
    }
}
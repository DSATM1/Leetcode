class Solution {
    public long maxAlternatingSum(int[] nums) {
        int n = nums.length;
        long[] squares = new long[n];
        
        // Square each element, as the sign doesn't matter
        for (int i = 0; i < n; i++) {
            squares[i] = (long) nums[i] * nums[i];
        }
        
        // Sort the squares in ascending order
        java.util.Arrays.sort(squares);
        
        long maxScore = 0;
        
        // To maximize the score, we want to subtract the smallest squares (odd indices)
        // and add the largest squares (even indices).
        // There will always be floor(n/2) negative terms and ceil(n/2) positive terms.
        for (int i = 0; i < n / 2; i++) {
            maxScore -= squares[i];
        }
        for (int i = n / 2; i < n; i++) {
            maxScore += squares[i];
        }
        
        return maxScore;
    }
}
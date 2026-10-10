class Solution {
    public long minSumSquareDiff(int[] nums1, int[] nums2, int k1, int k2) {
        int n = nums1.length;
        // The maximum possible difference based on constraints is 10^5
        int[] diffCounts = new int[100001];
        long k = (long) k1 + k2; // Combine k1 and k2
        
        // Count the frequencies of each absolute difference
        for (int i = 0; i < n; i++) {
            int diff = Math.abs(nums1[i] - nums2[i]);
            diffCounts[diff]++;
        }
        
        // Greedily reduce the largest differences
        for (int i = 100000; i > 0 && k > 0; i--) {
            if (diffCounts[i] > 0) {
                // We can reduce at most 'k' elements, or all elements with difference 'i'
                long reduceAmount = Math.min((long) diffCounts[i], k);
                diffCounts[i] -= reduceAmount;
                diffCounts[i - 1] += reduceAmount;
                k -= reduceAmount;
            }
        }
        
        // Calculate the final sum of squared differences
        long ans = 0;
        for (long i = 1; i <= 100000; i++) {
            if (diffCounts[(int)i] > 0) {
                ans += diffCounts[(int)i] * (i * i);
            }
        }
        
        return ans;
    }
}
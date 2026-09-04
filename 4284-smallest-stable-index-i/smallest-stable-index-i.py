class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Precompute suffix minimums
        suffix_min = [0] * n
        current_min = float('inf')
        for i in range(n - 1, -1, -1):
            current_min = min(current_min, nums[i])
            suffix_min[i] = current_min
            
        # Iterate through each index and maintain prefix maximum
        current_max = float('-inf')
        for i in range(n):
            current_max = max(current_max, nums[i])
            instability_score = current_max - suffix_min[i]
            
            if instability_score <= k:
                return i
                
        return -1
from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        # dp[r] will store the number of subarrays ending at the current index 
        # with a product that has a remainder of r modulo k.
        dp = [0] * k
        ans = [0] * k
        
        for num in nums:
            next_dp = [0] * k
            
            # Extend existing subarrays ending at the previous index
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * num) % k
                    next_dp[new_r] += dp[r]
            
            # Start a new subarray at the current index
            next_dp[num % k] += 1
            
            # Add the counts of subarrays ending at the current index to our total answer
            for r in range(k):
                ans[r] += next_dp[r]
            
            # Move to the next index
            dp = next_dp
            
        return ans
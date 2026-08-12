from collections import defaultdict
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            count[nums[right]] += 1
            
            # Shrink window from the left until nums[right] frequency <= k
            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1
            
            # Update the maximum valid window size
            max_len = max(max_len, right - left + 1)
            
        return max_len
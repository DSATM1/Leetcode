class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        
        for i, num in enumerate(nums):
            # If the number was seen before and the index difference is <= k
            if num in seen and i - seen[num] <= k:
                return True
            # Update/store the latest index of the number
            seen[num] = i
            
        return False
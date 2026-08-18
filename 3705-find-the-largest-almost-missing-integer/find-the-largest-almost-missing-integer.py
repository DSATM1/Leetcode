from collections import Counter

class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        counts = Counter(nums)
        
        # Case 1: Subarray size is 1
        if k == 1:
            unique_elements = [x for x, count in counts.items() if count == 1]
            return max(unique_elements) if unique_elements else -1
            
        # Case 2: Subarray size is equal to array length
        if k == n:
            return max(nums)
            
        # Case 3: 1 < k < n
        candidates = []
        if counts[nums[0]] == 1:
            candidates.append(nums[0])
        if counts[nums[-1]] == 1:
            candidates.append(nums[-1])
            
        return max(candidates) if candidates else -1
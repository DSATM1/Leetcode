class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        n = len(nums)
        
        while i < n:
            start = nums[i]
            
            # Keep moving forward as long as numbers are consecutive
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            
            # Format the range based on whether start equals the end of the range
            if start == nums[i]:
                ans.append(str(start))
            else:
                ans.append(f"{start}->{nums[i]}")
            
            i += 1
            
        return ans
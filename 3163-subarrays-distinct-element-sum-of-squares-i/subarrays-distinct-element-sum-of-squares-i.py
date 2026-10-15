class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
        # Iterate over all possible starting points of subarrays
        for i in range(n):
            distinct_elements = set()
            # Expand the subarray ending at j and keep track of distinct elements
            for j in range(i, n):
                distinct_elements.add(nums[j])
                count = len(distinct_elements)
                total_sum += count * count
                
        return total_sum
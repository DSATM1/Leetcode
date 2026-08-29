class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        # Pair elements with their original indices and sort by value
        sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))
        
        result = [0] * n
        group_vals = []
        group_indices = []
        
        for i in range(n):
            val, idx = sorted_nums[i]
            
            # Start a new group if difference exceeds limit
            if group_vals and val - group_vals[-1] > limit:
                # Place sorted values into sorted original indices for the current group
                group_indices.sort()
                for g_idx, g_val in zip(group_indices, group_vals):
                    result[g_idx] = g_val
                
                group_vals = []
                group_indices = []
            
            group_vals.append(val)
            group_indices.append(idx)
        
        # Process the final group
        if group_vals:
            group_indices.sort()
            for g_idx, g_val in zip(group_indices, group_vals):
                result[g_idx] = g_val
                
        return result
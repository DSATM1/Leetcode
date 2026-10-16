class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Segment tree arrays
        tree_sum = [0] * (4 * n)
        tree_sq_sum = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def apply(node, start, end, val):
            length = end - start + 1
            # Update square sum: (a+v)^2 = a^2 + 2av + v^2
            # Sum of (a+v)^2 = sum(a^2) + 2v*sum(a) + v^2 * length
            tree_sq_sum[node] = (tree_sq_sum[node] + 2 * val * tree_sum[node] + val * val * length) % MOD
            # Update sum: sum(a+v) = sum(a) + v * length
            tree_sum[node] = (tree_sum[node] + val * length) % MOD
            lazy[node] = (lazy[node] + val) % MOD
            
        def push_down(node, start, end):
            if lazy[node] != 0:
                mid = (start + end) // 2
                apply(2 * node + 1, start, mid, lazy[node])
                apply(2 * node + 2, mid + 1, end, lazy[node])
                lazy[node] = 0
                
        def update(node, start, end, l, r, val):
            if l > end or r < start:
                return
            if l <= start and end <= r:
                apply(node, start, end, val)
                return
            
            push_down(node, start, end)
            mid = (start + end) // 2
            update(2 * node + 1, start, mid, l, r, val)
            update(2 * node + 2, mid + 1, end, l, r, val)
            
            tree_sum[node] = (tree_sum[2 * node + 1] + tree_sum[2 * node + 2]) % MOD
            tree_sq_sum[node] = (tree_sq_sum[2 * node + 1] + tree_sq_sum[2 * node + 2]) % MOD

        ans = 0
        last_seen = {}
        
        for i in range(n):
            # The range to increment is from the index after the last occurrence of nums[i] to i
            start_idx = last_seen.get(nums[i], -1) + 1
            
            # Add 1 to the distinct count for all subarrays starting in [start_idx, i] and ending at i
            update(0, 0, n - 1, start_idx, i, 1)
            
            # The root of the segment tree now holds the sum of squares of distinct counts for all subarrays ending at i
            ans = (ans + tree_sq_sum[0]) % MOD
            
            last_seen[nums[i]] = i
            
        return ans
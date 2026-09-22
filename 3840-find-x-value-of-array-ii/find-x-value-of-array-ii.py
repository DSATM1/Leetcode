from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # Segment tree arrays
        # tree_prod[i] stores the total product modulo k of the segment
        tree_prod = [0] * (4 * n)
        # tree_counts[i] stores an array of size k, where tree_counts[i][r] is the 
        # number of prefixes in this segment that have a product modulo k equal to r.
        tree_counts = [[0] * k for _ in range(4 * n)]

        def merge(left_prod: int, left_counts: List[int], right_prod: int, right_counts: List[int]):
            # The total product of the merged segment
            prod = (left_prod * right_prod) % k
            # Start with the prefix products from the left segment
            counts = left_counts[:]
            
            # Add the prefix products that extend into the right segment
            for j in range(k):
                if right_counts[j] > 0:
                    counts[(left_prod * j) % k] += right_counts[j]
                    
            return prod, counts

        def build(node: int, start: int, end: int):
            if start == end:
                val = nums[start] % k
                tree_prod[node] = val
                tree_counts[node][val] = 1
                return
                
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            
            p, c = merge(tree_prod[2 * node + 1], tree_counts[2 * node + 1],
                         tree_prod[2 * node + 2], tree_counts[2 * node + 2])
            tree_prod[node] = p
            tree_counts[node] = c

        def update(node: int, start: int, end: int, idx: int, val: int):
            if start == end:
                val_mod = val % k
                tree_prod[node] = val_mod
                # Reset the counts and set the new value
                for i in range(k):
                    tree_counts[node][i] = 0
                tree_counts[node][val_mod] = 1
                return
                
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node + 1, start, mid, idx, val)
            else:
                update(2 * node + 2, mid + 1, end, idx, val)
                
            p, c = merge(tree_prod[2 * node + 1], tree_counts[2 * node + 1],
                         tree_prod[2 * node + 2], tree_counts[2 * node + 2])
            tree_prod[node] = p
            tree_counts[node] = c

        def query(node: int, start: int, end: int, l: int, r: int):
            # Completely within range
            if l <= start and end <= r:
                return tree_prod[node], tree_counts[node]
                
            mid = (start + end) // 2
            # Only in left child
            if r <= mid:
                return query(2 * node + 1, start, mid, l, r)
            # Only in right child
            elif l > mid:
                return query(2 * node + 2, mid + 1, end, l, r)
            # Spans across both children, requires merging results
            else:
                lp, lc = query(2 * node + 1, start, mid, l, r)
                rp, rc = query(2 * node + 2, mid + 1, end, l, r)
                return merge(lp, lc, rp, rc)

        # Build the initial segment tree
        build(0, 0, n - 1)
        
        res = []
        for idx, val, start_i, x_i in queries:
            # 1. Update the value at index 'idx' to 'val'
            update(0, 0, n - 1, idx, val)
            
            # 2. Query the remainder frequencies for the subarray from 'start_i' to the end
            _, counts = query(0, 0, n - 1, start_i, n - 1)
            
            # 3. Store the number of prefix combinations that equal the target x_i
            res.append(counts[x_i])
            
        return res
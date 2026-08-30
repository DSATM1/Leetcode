class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        # Find 0-indexed positions of min and max elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Ensure i is the smaller index and j is the larger index
        i, j = min(min_idx, max_idx), max(min_idx, max_idx)

        # Scenario 1: Remove both from front
        from_front = j + 1

        # Scenario 2: Remove both from back
        from_back = n - i

        # Scenario 3: Remove one from front and one from back
        from_both = (i + 1) + (n - j)

        return min(from_front, from_back, from_both)
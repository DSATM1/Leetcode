from functools import reduce
import operator

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if not any(nums):
            return 0

        total_xor = reduce(operator.xor, nums)

        if total_xor != 0:
            return len(nums)

        return len(nums) - 1
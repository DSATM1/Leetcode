class Solution:
    def isGood(self, nums: list[int]) -> bool:
        # The maximum expected element 'n' is the length of the array minus 1
        n = len(nums) - 1
        
        # Sort the given array to compare it with the expected base sequence
        nums.sort()
        
        # Check if it exactly matches the expected sequence [1, 2, ..., n-1, n, n]
        return nums == list(range(1, n)) + [n, n]
class Solution(object):
    def rotate(self, nums, k):
        if len(nums) == 0:
            return 
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]







        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
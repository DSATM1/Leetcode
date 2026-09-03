class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Check if all elements already have the same parity (all even or all odd)
        all_same_parity = all(x % 2 == nums1[0] % 2 for x in nums1)
        if all_same_parity:
            return True
        
        # If all elements don't have the same parity, we can make all elements odd
        # if and only if the global minimum element of the array is odd.
        return min(nums1) % 2 != 0
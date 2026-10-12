class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 32
        
        # Count the occurrences of each bit position across all numbers
        for num in nums:
            for i in range(32):
                if (num >> i) & 1:
                    bit_counts[i] += 1
                    
        ans = 0
        
        # Greedily construct k largest possible numbers
        for _ in range(k):
            val = 0
            for i in range(32):
                if bit_counts[i] > 0:
                    val |= (1 << i)
                    bit_counts[i] -= 1
            
            # Add the square of the constructed number to the total sum
            ans = (ans + val * val) % MOD
            
        return ans
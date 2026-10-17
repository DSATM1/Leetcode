class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Helper function to calculate the digit sum using math operations
        def get_digit_sum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total
            
        n = len(nums)
        # Create an array of tuples: (digit_sum, value, original_index)
        arr = [(get_digit_sum(nums[i]), nums[i], i) for i in range(n)]
        
        # Sort based on digit sum first, then by value (inherent in tuple sorting)
        arr.sort()
        
        visited = [False] * n
        swaps = 0
        
        # Cycle detection to find the minimum number of swaps
        for i in range(n):
            # If already visited or already in the correct position, skip
            if visited[i] or arr[i][2] == i:
                continue
                
            cycle_size = 0
            j = i
            
            # Trace the cycle
            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_size += 1
                
            # If there is a cycle of length > 1, it takes (cycle_size - 1) swaps to resolve
            if cycle_size > 1:
                swaps += cycle_size - 1
                
        return swaps
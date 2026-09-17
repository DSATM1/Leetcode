class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # best_till[i] will store the minimum length of a valid subarray ending at or before index i
        best_till = [float('inf')] * n 
        ans = float('inf')
        best_len = float('inf')
        
        left = 0
        window_sum = 0
        
        for right in range(n):
            window_sum += arr[right]
            
            # Shrink the window from the left if the sum exceeds the target
            while window_sum > target and left <= right:
                window_sum -= arr[left]
                left += 1
                
            # If we find a valid subarray
            if window_sum == target:
                curr_len = right - left + 1
                
                # Check if there's a valid non-overlapping subarray before our current window's left bound
                if left > 0 and best_till[left - 1] != float('inf'):
                    ans = min(ans, curr_len + best_till[left - 1])
                
                # Update the overall minimum length seen so far
                best_len = min(best_len, curr_len)
            
            # Record the best minimum length up to the current index
            best_till[right] = best_len
            
        return ans if ans != float('inf') else -1
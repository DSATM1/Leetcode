import heapq

class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # Pair elements from nums1 and nums2, then sort by nums2 in descending order
        pairs = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
        
        min_heap = []
        current_sum = 0
        max_score = 0
        
        for n1, n2 in pairs:
            heapq.heappush(min_heap, n1)
            current_sum += n1
            
            # Keep only the k largest elements from nums1 in the heap
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)
            
            # When we have exactly k elements, compute the score
            if len(min_heap) == k:
                max_score = max(max_score, current_sum * n2)
                
        return max_score
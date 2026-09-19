import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        # Pair up the capital and profits, and sort them based on the required capital
        projects = sorted(zip(capital, profits))
        
        max_heap = []
        ptr = 0
        n = len(profits)
        
        for _ in range(k):
            # Push all projects we can afford with our current capital into the max-heap
            while ptr < n and projects[ptr][0] <= w:
                # Python's heapq is a min-heap, so we negate the profit to simulate a max-heap
                heapq.heappush(max_heap, -projects[ptr][1])
                ptr += 1
            
            # If there are no projects we can afford, we must stop early
            if not max_heap:
                break
                
            # Pop the project with the maximum profit and add it to our current capital
            w -= heapq.heappop(max_heap)
            
        return w
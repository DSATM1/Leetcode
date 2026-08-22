import heapq


class Solution:

    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        head = []
        tail = []

        i = 0
        j = len(costs) - 1

        # Fill initial candidate pools
        while i < candidates:
            heapq.heappush(head, costs[i])
            i += 1

        while j >= i and len(tail) < candidates:
            heapq.heappush(tail, costs[j])
            j -= 1

        total_cost = 0

        # Hire k workers
        for _ in range(k):
            if not tail or (head and head[0] <= tail[0]):
                total_cost += heapq.heappop(head)
                if i <= j:
                    heapq.heappush(head, costs[i])
                    i += 1
            else:
                total_cost += heapq.heappop(tail)
                if i <= j:
                    heapq.heappush(tail, costs[j])
                    j -= 1

        return total_cost
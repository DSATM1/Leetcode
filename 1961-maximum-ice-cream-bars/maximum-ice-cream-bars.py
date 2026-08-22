class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if not costs:
            return 0
        max_cost = max(costs)

    
        freq = [0] * (max_cost + 1)
        for cost in costs:
            freq[cost] += 1

        total_bars = 0

        for price in range(1, max_cost + 1):
            if freq[price] == 0:
                continue

            if coins < price:
                break

            aff_count = coins // price
            bars_to_buy = min(freq[price], aff_count)

            total_bars += bars_to_buy
            coins -= price * bars_to_buy
        
        return total_bars 
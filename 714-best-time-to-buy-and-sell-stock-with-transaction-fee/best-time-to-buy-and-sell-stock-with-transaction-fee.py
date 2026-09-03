class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # hold: max profit if we currently own a stock
        hold = -prices[0]
        # cash: max profit if we currently do not own a stock
        cash = 0
        
        for price in prices[1:]:
            # Either we keep our previous cash state, or we sell the stock we were holding
            cash = max(cash, hold + price - fee)
            # Either we keep our previous hold state, or we buy the stock using current cash
            hold = max(hold, cash - price)
            
        return cash
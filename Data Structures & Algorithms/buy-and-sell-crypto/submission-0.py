class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        buy_price = prices[0]
        prof_max = 0
        while sell < len(prices):
            buy_price = min(buy_price, prices[sell])
            prof_max = max(prices[sell]-buy_price, prof_max)
            sell+=1
        return prof_max
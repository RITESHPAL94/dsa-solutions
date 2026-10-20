class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_prices = prices[0]
        total = 0
        for price in prices:
            min_prices = min(min_prices,price)
            profit = price - min_prices
            total = max(total,profit)
        return total
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = prices[0]
        for price in prices:
            mini = min(mini, price)
            profit = max(profit, price - mini)
        return profit
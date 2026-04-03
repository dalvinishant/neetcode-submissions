class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        for i in range(0, len(prices)):
            max_p = max(max_p, self.buyAndSell(i, prices))
        return max_p
    
    def buyAndSell(self, i, prices):
        if i >= len(prices):
            return 0
        profit = 0
        for j in range(i, len(prices)):
            profit = max(profit, prices[j] - prices[i])

        return profit

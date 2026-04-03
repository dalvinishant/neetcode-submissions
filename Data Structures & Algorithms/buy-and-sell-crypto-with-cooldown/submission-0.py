class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.buyAndSell(0,prices, True, {})
    
    def buyAndSell(self, i, prices, buy, mem):
        if i >= len(prices):
            return 0
        
        if (i, buy) in mem:
            return mem[(i, buy)]

        # not buy and not sell
        cooldown = self.buyAndSell(i+1, prices, buy, mem)

        max_p = 0
        if buy:
            # buy
            profit = self.buyAndSell(i+1, prices, not buy, mem) - prices[i]
            max_p = max(cooldown, profit)
            mem[(i, buy)] = max_p
        else:
            #sell
            profit = self.buyAndSell(i+2, prices, not buy, mem) + prices[i]
            max_p = max(cooldown, profit)
            mem[(i, buy)] = max_p

        return max_p
from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0
        print(dp)
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i and dp[i - coins[j]] != inf:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        print(dp)
        return -1 if dp[amount] == inf else dp[amount]
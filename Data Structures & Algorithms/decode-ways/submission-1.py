class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[-1] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                continue
            elif i + 1 < n and 1 <= int(s[i] + s[i+1]) <= 26:
                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]
        return dp[0]
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initial
        if amount == 0:
            return 0
        
        #+1: starting from 1
        dp = [float("inf") for _ in range(amount+1)]
        dp[0] = 0
        
        #dp: i amount, value: minimum path
        for c in coins:
            if c < amount+1:
                dp[c] = 1

        for n in range(1, amount+1):
            for coin in coins:
                if n-coin > 0:
                    dp[n] = min(dp[n-coin] + 1, dp[n])
                else:
                    continue
        
        return dp[n] if dp[n] != float("inf") else -1
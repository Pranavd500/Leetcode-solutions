class Solution:
    def change(self, amount: int, coins: list[int]) -> int:

        # dp[i] = number of ways to make amount i
        dp = [0] * (amount + 1)

        # One way to make amount 0 (choose no coins)
        dp[0] = 1

        # Process one coin at a time
        for coin in coins:

            # Update all reachable amounts
            for curr in range(coin, amount + 1):
                dp[curr] += dp[curr - coin]

        return dp[amount]
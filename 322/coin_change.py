#!/usr/bin/env python3

class Solution:
    def __init__(self):
        self.dp = [None] * 10001
        self.dp[0] = 0

    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return self.dp[0]
        if amount < 0:
            return -1

        if self.dp[amount] is not None: return self.dp[amount]

        m = 10002
        for x in coins:
            cc = self.coinChange(coins, amount-x)
            if cc == -1: continue
            m = min(m, cc)

        self.dp[amount] = m + 1
        if m == 10002: self.dp[amount] = -1
        return self.dp[amount]


print(Solution().coinChange([1, 2, 5], 11))
print(Solution().coinChange([1, 2, 5], 1))
print(Solution().coinChange([2], 3))

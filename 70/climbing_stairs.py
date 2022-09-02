#!/usr/bin/env python3

class Solution:
    def __init__(self):
        self.dp = [None] * 46
        self.dp[1] = 1
        self.dp[2] = 2

    def climbStairs(self, n: int) -> int:
        if self.dp[n] is not None:
            return self.dp[n]

        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]

print(Solution().climbStairs(38))

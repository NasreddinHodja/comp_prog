#!/usr/bin/env python3

class Solution:
    def __init__(self):
        self.dp = []
        for i in range(1002):
            new_vec = [None] * 1002
            self.dp.append(new_vec)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        for i in range(0, len(self.dp)):
            self.dp[i][0] = 0
            self.dp[0][i] = 0

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    self.dp[i][j] = 1 + self.dp[i-1][j-1]
                else:
                    self.dp[i][j] = max(self.dp[i-1][j], self.dp[i][j-1])

        return self.dp[len(text1)][len(text2)]

# print(Solution().longestCommonSubsequence("ylqpejqbalahwr", "yrkzavgdmdgtqpg"))
# print(Solution().longestCommonSubsequence("bl", "yby"))
print(Solution().longestCommonSubsequence("ezupkr", "ubmrapg"))
# print(Solution().longestCommonSubsequence("abcba", "abcbcba"))
# print(Solution().longestCommonSubsequence("abcde", "ace"))

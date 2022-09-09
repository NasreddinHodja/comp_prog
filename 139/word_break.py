#!/usr/bin/env python3

class Solution:
    def __init__(self):
        self.dp = [None] * 301

    def wordBreak(self, s: str, word_dict: list[str]) -> bool:
        if self.dp[len(s)] is not None:
            return self.dp[len(s)]

        for word in word_dict:
            if word == s[:len(word)]:
                if len(word) == len(s):
                    self.dp[len(s)] = True
                    return True
                if self.wordBreak(s[len(word):], word_dict):
                    self.dp[len(s)] = True
                    return True
        self.dp[len(s)] = False
        return False


print(Solution().wordBreak("leetcode", ["leet", "code"]))
print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

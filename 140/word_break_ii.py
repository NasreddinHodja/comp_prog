#!/usr/bin/env python3

class Solution:
    def __init__(self):
        self.dp = [[]] * 301

    def wordBreak(self, s: str, word_dict: list[str], parted = []) -> bool:
        for word in word_dict:
            if word == s[:len(word)]:
                if len(word) == len(s):
                    self.dp[len(s)] += [" ".join(parted + [word])]
                    continue

                wb = self.wordBreak(s[len(word):], word_dict, parted + [word])
        # for word in word_dict:
        #     if word == s[:len(word)]:
        #         if len(word) == len(s):
        #             if self.dp[len(s)] is None:
        #                 self.dp[len(s)] = []

        #             self.dp[len(s)] += [" ".join(parted + [word])]
        #             return self.dp[len(s)]

        #         if self.wordBreak(s[len(word):], word_dict, parted):
        #             if self.dp[len(s)] is None:
        #                 self.dp[len(s)] = []

        #             self.dp[len(s)] += [" ".join(parted + [word])]
        #             return self.dp[len(s)]

        return self.dp[len(s)]

print(Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))
print(Solution().wordBreak("pineapplepenapple",
                           ["apple","pen","applepen","pine","pineapple"]))
print(Solution().wordBreak("catsandog",
                           ["cats","dog","sand","and","cat"]))

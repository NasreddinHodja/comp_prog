#!/usr/bin/env python3

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        letter_counts = {}
        anagrams = {}

        for word in strs:
            curr_count = [0] * 26

            for l in word:
                curr_count[ord(l) - ord("a")] += 1


            added = False
            for w, count  in letter_counts.items():
                if curr_count == count:
                    anagrams[w] += [word]
                    added = True

            if not added:
                anagrams[word] = [word]
                letter_counts[word] = curr_count

        return list(anagrams.values())


s = Solution()
print(s.groupAnagrams(["a"]))

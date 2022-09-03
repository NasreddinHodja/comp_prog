#!/usr/bin/env python3

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ans = 0
        s = set(nums)

        for i in range(len(nums)):
            if nums[i] - 1 not in s:
                j = nums[i]

                while j in s:
                    j += 1

                ans = max(ans, j - nums[i])

        return ans


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))

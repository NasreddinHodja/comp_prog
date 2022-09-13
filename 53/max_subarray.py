#!/usr/bin/env python3

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        result = nums[0]
        curr = nums[0]

        for i in range(1, len(nums)):
            curr = max(curr+nums[i], nums[i])
            result = max(result, curr)

        return result

print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

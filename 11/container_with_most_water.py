#!/usr/bin/env python3

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max = 0
        i, j = 0, len(height) - 1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if area > max: max = area

            if height[i] > height[j]: j -= 1
            else: i += 1

        return max

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))

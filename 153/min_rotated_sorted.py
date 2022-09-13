#!/usr/bin/env python3

class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        m = float("inf")

        while l <= r:
            mid = int(l + (r - l) / 2)
            m = min(m, nums[mid])

            if nums[mid] >= nums[l] and nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return m

# print(Solution().findMin([3, 4, 5, 1, 2]))
print(Solution().findMin([4,5,6,7,0,1,2]))

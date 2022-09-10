#!/usr/bin/env python3

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result = []

        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                j = i + 1
                k = len(nums) - 1

                while j < k:
                    sum = nums[j] + nums[k]

                    if sum == -nums[i]:
                        result.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j+1] : j += 1
                        j += 1
                        while j < k and nums[k] == nums[k-1] : k -= 1
                        k -= 1
                    elif sum < -nums[i]:
                        j += 1
                    else:
                        k -= 1

        return result

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([1, -1, -1, 0]))

#!/usr/bin/env python3

class Solution:
    # def maxProduct(self, nums: list[int]) -> int:
    #     result = float("-inf")
    #     pos, neg = 0, 0
    #     for i in range(len(nums)):
    #         if nums[i] < 0:
    #             temp = pos
    #             pos = neg
    #             neg = temp

    #         if pos != 0: pos *= nums[i]
    #         elif nums[i] > 0: pos = nums[i]
    #         else: pos = 0

    #         if neg != 0: neg *= nums[i]
    #         elif nums[i] < 0: neg = nums[i]
    #         else: neg = 0

    #         if pos > 0 and pos > result: result = pos
    #         if nums[i] > result: result = nums[i]

    #     return result

    def maxProduct(self, nums: list[int]) -> int:
        if len(nums) == 0: return 0

        result = float("-inf")
        curr_a = 0
        curr_b = 0

        for i in range(1, len(nums)):

            if curr_a != 0:

            curr = max(nums[i], curr * nums[i])

            result = max(result, curr)

        return result

print(Solution().maxProduct([2, 3, -2, 4]))
print(Solution().maxProduct([-2,0,-1]))
print(Solution().maxProduct([]))
print(Solution().maxProduct([-2]))
print(Solution().maxProduct([1,0,-1,2,3,-5,-2]))

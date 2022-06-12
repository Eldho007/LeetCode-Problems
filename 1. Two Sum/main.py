# Leetcode Chalenege 1 - Given an array of integers nums and an integer target, return indices of the two numbers such
# that they add up to target. You may assume that each input would have exactly one solution, and you may not use the
# same element twice. You can return the answer in any order.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        values = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    values = [i, j]
                    return values


test = Solution()
test.twoSum([1, 2, 3], 5)

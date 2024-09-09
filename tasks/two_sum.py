# Link -> https://leetcode.com/problems/two-sum/description/
# Author: Ilya Shvarev
class Solution:
    def twoSum(self, nums: list[int], target: int):
        num_map = {}
        for index, num in enumerate(nums):
            ext = target - num
            if ext in num_map:
                return [num_map[ext], index]
            num_map[num] = index
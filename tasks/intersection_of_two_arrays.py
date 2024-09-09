# Link -> https://leetcode.com/problems/intersection-of-two-arrays
# Author: Ilya Shvarev


from typing import List

class Solution:
    @staticmethod
    def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        n2 = set(nums2)
        n1 = set(nums1)

        lst = []

        for item in n1:
            if item in n2:
                lst.append(item)
        return lst


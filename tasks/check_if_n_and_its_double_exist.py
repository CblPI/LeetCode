# Link -> https://leetcode.com/problems/check-if-n-and-its-double-exist
# Author: Ilya Shvarev


from typing import List


class Solution:
    @staticmethod
    def checkIfExist(arr: List[int]) -> bool:
        seen = set()
        for item in arr:
            if item * 2 in seen or item / 2 in seen:
                return True
            seen.add(item)
        return False

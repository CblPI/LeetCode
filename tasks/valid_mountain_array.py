# Link -> https://leetcode.com/problems/valid-mountain-array
# Author: Ilya Shvarev


from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)

        if n < 3:
            return False

        i = 0
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == n - 1:
            return False

        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1
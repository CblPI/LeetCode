# Link -> https://leetcode.com/problems/first-unique-character-in-a-string
# Author: Ilya Shvarev

from collections import Counter


class Solution:
    @staticmethod
    def firstUniqChar(s: str) -> int:
        counted_map = Counter(s)
        if 1 not in counted_map.values():
            return -1
        for k, v, in counted_map.items():
            if v == 1: return s.index(k)

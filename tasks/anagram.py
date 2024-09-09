# Link -> https://leetcode.com/problems/valid-anagram/
# Author: Ilya Shvarev


class Solution:
    @staticmethod
    def isAnagram(target: str, sub: str) -> bool:
        if len(target) < len(sub): return False
        sorted_s = sorted(target)
        sorted_t = sorted(sub)
        return sorted_s == sorted_t

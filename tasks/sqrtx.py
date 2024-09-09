# Link -> https://leetcode.com/problems/sqrtx
# Author: Ilya Shvarev


class Solution:
    @staticmethod
    def mySqrt(x: int) -> int:
        if x == 0:
            return 0
        pre = x / 2.0
        while True:
            curr = (pre + x / pre) / 2
            if abs(curr - pre) < .00000001:
                return int(curr)
            pre = curr
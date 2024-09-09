# Link -> https://leetcode.com/problems/first-bad-version
# Author: Ilya Shvarev

_target = 0


def set_target(value: int):
    global _target
    _target = value

def isBadVersion(version: int) -> bool: # pragma: nocover
    return True if version >= _target else False


class Solution:
    @staticmethod
    def firstBadVersion(right: int) -> int:
        if right == 1:
            return right

        start = 1
        badVersion = 1

        while start <= right:
            mid = start + (right - start) // 2
            if isBadVersion(mid):
                badVersion = mid
                right = mid - 1
            else:
                start = mid + 1

        return badVersion

import pytest

from tasks.two_sum import Solution


@pytest.mark.parametrize(
    "lst1, target, result", [
        ([1, 5, 12, 6], 11, [1, 3]),
        ([4, 9, 17, 4, 5, 14], 21, [0, 2])
    ]
)
def test_two_sum(lst1, target, result):
    sol = Solution()
    assert sol.twoSum(lst1, target) == result
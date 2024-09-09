import pytest

from tasks.valid_mountain_array import Solution


@pytest.mark.parametrize(
    "array, result", [
        ([0, 2, 3, 4, 3, 2, 1], True),
        ([15, 25, 125, 555, 125, 5, 1], True),
        ([15, 25, 125, 555, 125, 244, 555], False),
        ([15, 25, 44, 45, 34], True)
    ]
)
def test_mountain(array, result):
    assert Solution().validMountainArray(array) is result
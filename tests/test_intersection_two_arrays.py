import pytest

from tasks.intersection_of_two_arrays import Solution

@pytest.mark.parametrize(
    "list1, list2, result", [
        (
            [1, 2, 2, 1],
            [2, 2],
            [2]
        ),
        (
            [2, 1, 5, 4],
            [1, 2, 5, 4],
            [1, 2, 4, 5]
        ),
        (
            [5, 1, 2, 4, 6, 1, 7],
            [7, 1, 6, 5, 2, 4],
            [1, 2, 4, 5, 6, 7]
        )
    ]
)
def test_intersection_two_arrays(list1, list2, result):
    assert Solution.intersection(list1, list2) == result
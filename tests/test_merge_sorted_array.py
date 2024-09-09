import pytest

from tasks.merge_sorted_array import Solution


@pytest.mark.parametrize(
    "lst1, m1, lst2, m2, result", [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([6, 7, 8, 0, 0, 0], 3, [2, 5, 6], 3, [2, 5, 6, 6, 7, 8])
    ]
)
def test_merge_array(lst1, m1, lst2, m2, result):
    Solution.merge(lst1, m1, lst2, m2)
    assert lst1 == result

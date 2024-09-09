import pytest

from structures.LIST import ListNode
from tasks.add_two_numbers import Solution


@pytest.mark.parametrize(
    "first, second, result", [
        (
            [1, 2, 3],
            [1, 2, 3],
            [2, 4, 6]
        ),
        (
            [9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9],
            [8, 9, 9, 9, 0, 0, 0, 1]
        ),
        (
            [1],
            [5, 4, 0],
            [6, 4, 0],
        ),
        (
            [1],
            [9, 9, 9, 9, 9, 9],
            [0, 0, 0, 0, 0, 0, 1]
        )
    ]
)
def test_add_two_numbers(first, second, result):
    lst1 = ListNode()
    lst1.fill(first)
    assert lst1.get_list() == first

    lst2 = ListNode()
    lst2.fill(second)
    assert lst2.get_list() == second

    result_lst = Solution.addTwoNumbers(lst1, lst2)

    assert result == result_lst.get_list()


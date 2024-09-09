import pytest

from structures.LIST import ListNode
from tasks.merge_two_sorted_lists import Solution


@pytest.mark.parametrize(
    "lst1, lst2, result", [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([5, 5, 5], [2, 8, 9], [2, 5, 5, 5, 8, 9])
    ]
)
def test_merged_two_lists(lst1, lst2, result):
    ls1 = ListNode()
    ls1.fill(lst1)

    ls2 = ListNode()
    ls2.fill(lst2)

    assert Solution.mergeTwoLists(ls1, ls2).get_list() == result
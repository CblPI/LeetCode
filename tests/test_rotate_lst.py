import pytest

from structures.LIST import ListNode
from tasks.rotate_list import Solution

@pytest.mark.parametrize(
    "lst, count, result", [
        ([1, 2, 3 ,4 ,5], 1, [5, 1, 2, 3, 4]),
        ([1, 2, 3 ,4 ,4], 3, [3, 4, 4, 1, 2]),
        ([1, 2, 3 ,4 ,4], 0, [1, 2, 3, 4, 4])
    ]
)
def test_rotate_lst(lst, count, result):
    node = ListNode()
    node.fill(lst)
    assert Solution.rotateRight(node, count).get_list() == result
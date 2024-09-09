import pytest

from structures.LIST import ListNode
from tasks.linked_list_cycle_ii import Solution


@pytest.mark.parametrize(
    "lst, index, val, is_cycled", [
        ([3, 2, 0, 4], 1, 2, True),
        ([3, 1], 1, 1, True),
        ([3, 1], 1, 1, False)
    ]
)
def test_linked_list_cycle(lst, index, val, is_cycled):
    node = ListNode()
    node.fill(lst)
    if is_cycled:
        conn = node.get_elem(index)
        node.get_elem(50000).next = conn
        assert Solution.detectCycle(node).val == val
    else:
        assert Solution.detectCycle(node) == None




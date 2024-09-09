import pytest

from structures.LIST import ListNode
from tasks.palindrome_linked_list import Solution


@pytest.mark.parametrize(
    "lst, result", [
        ([1, 2, 2, 1], True),
        ([1, 2, 2, 2], False)
    ]
)
def test_palindrome_linked_list(lst, result):
    node = ListNode()
    node.fill(lst)
    assert Solution.isPalindrome(node) is result

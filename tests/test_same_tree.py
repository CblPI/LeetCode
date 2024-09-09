import pytest

from structures.BST import TreeNode
from tasks.same_tree import Solution


@pytest.mark.parametrize(
    "lst1, lst2, result", [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True),
        ([1, 2, 3, 4, 5], [1, 2, 6, 4, 5], False)
    ]
)
def test_same_tree(lst1, lst2, result):
    node1 = TreeNode()
    node1.fill(lst1)

    node2 = TreeNode()
    node2.fill(lst2)
    sol = Solution()
    assert sol.isSameTree(node1, node2) is result
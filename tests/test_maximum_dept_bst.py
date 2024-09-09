import pytest

from structures.BST import TreeNode
from tasks.maximum_depth_of_binary_tree import Solution


@pytest.mark.parametrize(
    "lst, result", [
        ([1, 5, 2, 6], 3),
        ([5, 12, 7, 24, 66, 12, 8, 123, 55], 6)
    ]
)
def test_max_depth(lst, result):
    node = TreeNode()
    node.fill(lst)
    assert Solution.maxDepth(node) == result
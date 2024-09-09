import pytest

from structures.BST import TreeNode
from tasks.minimum_depth_of_binary_tree import Solution


@pytest.mark.parametrize(
    "lst, result", [
        ([5, 4, 2, 3], 2),
        ([5, 6, 12, 2], 1)
    ]
)
def test_min_depth_bst(lst, result):
    node = TreeNode()
    node.fill(lst)

    assert Solution.minDepth(node) == 2



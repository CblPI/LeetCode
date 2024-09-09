import pytest

from structures.BST import TreeNode
from tasks.binary_tree_inorder_traversal import Solution


@pytest.mark.parametrize(
    "case, result", [
        ([1, 2, 3], [1, 2, 3, 4]),
        ([1, 2, 3, 5, 8, 6, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
    ]
)
def test_inorder_traversal(case, result):
    node = TreeNode()
    node.fill(case)
    assert Solution.inorderTraversal(node) == result
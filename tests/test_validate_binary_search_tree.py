import pytest

from structures.BST import TreeNode
from tasks.validate_binary_search_tree import Solution

case1 = TreeNode()
case1.fill([5, 4, 3, 7, 1])

case2 = TreeNode()
case2.fill_only_left([5, 9, 3, 7, 1])

@pytest.mark.parametrize(
    "node, result", [
        (case1, True),
        (case2, False)
    ]
)
def test_validate_bst(node: TreeNode, result):
    assert Solution.isValidBST(node) is result
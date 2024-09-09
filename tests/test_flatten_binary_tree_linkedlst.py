import pytest

from structures.BST import TreeNode
from tasks.flatten_binary_tree_to_linked_list import Solution


@pytest.mark.parametrize(
        "lst", [
        [1, 2, 3, 6, 5]
    ]
)
def test_flatten_bin_tree_lst(lst):
    node = TreeNode()
    node.fill(lst)
    sol = Solution()
    sol.flatten(node)

    node_right = TreeNode()
    node_right.fill_only_right(lst)

    assert node.get_right_lst() ==  node_right.get_right_lst()
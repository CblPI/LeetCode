import pytest

from structures.BST import TreeNode
from tasks.path_sum import Solution


@pytest.mark.parametrize(
    "nodes, summ, result", [
        ([5, 10], 19, True),
        ([8, 7, 12, 6, 55, 1], 19, False),
        ([3, 7, 2, 8, 1], 10, True)
    ]
)
def test_path_sum(nodes, summ, result):
    node = TreeNode()
    node.fill(nodes)
    assert Solution.hasPathSum(node, summ) is result
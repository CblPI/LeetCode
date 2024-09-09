from typing import Optional

import pytest

from tasks.add_one_row_to_tree import Solution
from structures.BST import TreeNode

@pytest.mark.parametrize(
    "depth, val, lst, in_mem, result, root_is", [
        (
            2,
            1,
            [4, 2, 6, 3, 1, 5],
            [4, 2, 6, 1, 3, 5],
            [4, 1, 1, 2, 6, 1, 3, 5],
            True
        ),
        (
            3,
            1,
            [4, 2, 3, 1],
            [4, 2, 1, 3],
            [4, 2, 1, 1, 1, 3],
            True
        ),
        (
            3,
            1,
            [4, 2, 3, 1],
            [4, 2, 1, 3],
            [4, 2, 1, 3],
            False
        ),
        (
            1,
            1,
            [4, 2, 3, 1],
            [4, 2, 1, 3],
            [4, 2, 1, 3],
            True
        ),
    ]
)
def test_add_one_row_to_tree(
        depth: int,
        val: int,
        lst: list[Optional[int]],
        result: list[Optional[int]],
        in_mem: list[Optional[int]], root_is) -> None:

    node1 = TreeNode()
    node1.fill(lst)
    assert node1.get_list() == in_mem

    Solution.addOneRow(node1 if root_is else None, val, depth)

    assert node1.get_list() == result


# Link -> https://leetcode.com/problems/add-one-row-to-tree
# Author: Ilya Shvarev

from typing import Optional

from structures.BST.tree import TreeNode


class Solution:
    @staticmethod
    def addOneRow(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def _go_depth(root: TreeNode, val: int, depth: int):
            if root is None:
                return

            if depth == 2:
                root.right = TreeNode(val, right=root.right)
                root.left = TreeNode(val, left=root.left)
                return

            _go_depth(root.left, val, depth - 1)
            _go_depth(root.right, val, depth - 1)

        if depth == 1:
            return TreeNode(val, root)

        _go_depth(root, val, depth)
        return root

# Link on quest -> https://leetcode.com/problems/binary-tree-inorder-traversal/
# Author: Ilya Shvarev


from typing import Optional, List

from tasks.flatten_binary_tree_to_linked_list import TreeNode


class Solution:
    @staticmethod
    def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
        result, lst = [], []
        current = root

        while current or lst:
            while current:
                lst.append(current)
                current = current.left

            current = lst.pop()
            result.append(current.val)
            current = current.right

        return result
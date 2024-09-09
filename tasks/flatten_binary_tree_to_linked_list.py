# Link -> https://leetcode.com/problems/flatten-binary-tree-to-linked-list
# Author: Ilya Shvarev


from typing import Optional

from structures.BST import TreeNode


class Solution:

    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return

        lst = []

        if root.left is not None:
            if root.right is not None:
                lst.append(root.right)
            temp = root.left
            root.left = None
            root.right = temp

        self.flatten(root.right)

        if root.right is not None:
            only_right = root.right

            while only_right.right is not None:
                only_right = only_right.right

            while lst:
                only_right.right = lst.pop()
                self.flatten(only_right.right)

    # @staticmethod
    # def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    #     def search_path_tree(node: Optional[TreeNode], current_sum: int) -> bool:
    #         if not node:
    #             return False
    #
    #         current_sum += node.val
    #
    #         if not node.left and not node.right:
    #             return current_sum == targetSum
    #
    #         return (search_path_tree(node.left, current_sum) or search_path_tree(node.right, current_sum))
    #
    #     return search_path_tree(root, 0)


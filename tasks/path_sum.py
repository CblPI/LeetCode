# Link -> https://leetcode.com/problems/path-sum
# Author: Ilya Shvarev


from typing import Optional

from structures.BST import TreeNode


class Solution:
    @staticmethod
    def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
        def search_path_tree(node: Optional[TreeNode], current_sum: int) -> bool:
            if not node:
                return False

            current_sum += node.val

            if not node.left and not node.right:
                return current_sum == targetSum

            return (search_path_tree(node.left, current_sum) or search_path_tree(node.right, current_sum))

        return search_path_tree(root, 0)
# Link -> https://leetcode.com/problems/validate-binary-search-tree
# Author: Ilya Shvarev

from structures.BST import TreeNode


class Solution:
    @staticmethod
    def isValidBST(root: TreeNode) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (validate(node.left, low, node.val) and validate(node.right, node.val, high))

        return validate(root)
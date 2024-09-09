# Link -> https://leetcode.com/problems/symmetric-tree
# Author: Ilya Shvarev


from structures.BST import TreeNode


class Solution:
    @staticmethod
    def isSymmetric(root: TreeNode) -> bool:
        def _symmetric(left: TreeNode, right: TreeNode) -> bool:
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False

            return (left.val == right.val) and _symmetric(left.left, right.right) and _symmetric(left.right, right.left)

        if not root:
            return True

        return _symmetric(root.left, root.right)
# Link -> https://leetcode.com/problems/minimum-depth-of-binary-tree
# Author: Ilya Shvarev


from collections import deque

from structures.BST import TreeNode


class Solution:
    @staticmethod
    def minDepth(root: TreeNode) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))
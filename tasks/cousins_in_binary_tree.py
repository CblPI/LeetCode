# Link ->  https://leetcode.com/problems/cousins-in-binary-tree
# Author: Ilya Shvarev

from collections import deque

from structures.BST import TreeNode


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False

        queue = deque([(root, None, 0)])

        parent_a = parent_b = None
        depth_x = depth_b = -1

        while queue:
            node, parent, depth = queue.popleft()

            if node.val == x:
                parent_a, depth_x = parent, depth
            elif node.val == y:
                parent_b, depth_b = parent, depth

            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))

            if depth_x != -1 and depth_b != -1:
                break
        return (depth_x == depth_b) and (parent_a != parent_b)
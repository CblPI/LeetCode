# Link -> https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Author: Shvarev Ilya


from typing import Optional

from structures.BST import TreeNode



class Solution:
    @staticmethod
    def maxDepth(root: Optional[TreeNode]) -> int:
        def to_depth(node: Optional[TreeNode], depth: int) -> int:
            if node:
                depth += 1
                val = to_depth(node.left, depth)
                val2 = to_depth(node.right, depth)
                return val2 if val2 > val else val
            return depth
        return to_depth(root, 0)
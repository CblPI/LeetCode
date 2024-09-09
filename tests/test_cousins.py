from structures.BST import TreeNode
from tasks.cousins_in_binary_tree import Solution


def test_cousins():
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.left.right = TreeNode(4)
    node.right = TreeNode(3)

    sol = Solution()

    assert sol.isCousins(node, 4, 3) is False
from structures.BST import TreeNode
from tasks.symmetric_tree import Solution


def test_symmetric():
    node = TreeNode(1)
    node.right = TreeNode(2)
    node.left = TreeNode(2)

    node.right.right = TreeNode(3)
    node.left.left = TreeNode(3)

    node.left.right = TreeNode(4)
    node.right.left = TreeNode(4)

    assert Solution.isSymmetric(node)

    node.left.right = TreeNode(3)
    node.left.left = TreeNode(4)

    assert Solution.isSymmetric(node) is False
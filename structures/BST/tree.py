class TreeNode:
    """Node"""

    # -- BASE PART --
    def __init__(self, val=4, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # -- CUSTOM PART --
    def __repr__(self):
        return f'{self.get_list()}'

    def fill(self, lst: list):
        for item in lst:
            self.append(item)
    def fill_only_left(self, lst: list):
        node = self
        for item in lst:
            node.left = TreeNode(item)
            node = node.left

    def get_right_lst(self):
        if not self:
            return
        resulted = []
        node = self

        while node:
            resulted.append(node.val)
            node = node.right


        return resulted

    def fill_only_right(self, lst: list):
        node = self
        for item in lst:
            node.right = TreeNode(item)
            node = node.right

    def get_list(self):
        if not self:
            return
        resulted = []
        queue = [self]

        while queue:
            current = queue.pop(0)
            resulted.append(current.val)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return resulted

    def append(self, value):
        if self is None:
            self.val = value
        else:
            self._add_recursive(self, value)

    def _add_recursive(self, node, value):
        if value < node.val:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._add_recursive(node.left, value)
        elif value > node.val:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._add_recursive(node.right, value)

    def seek(self, val: int):
        return self.__seek(self, None, val)

    def __seek(self, node: 'TreeNode', parent, value):
        if node is None:
            return None, parent, False

        if value == node.val:
            return node, parent, True

        if value < node.val:
            if node.left:
                return self.__seek(node.left, node, value)

        if value > node.val:
            if node.right:
                return self.__seek(node.right, node, value)

        return node, parent, False
from collections.abc import Iterable


class ListNode:
    """Node"""

    def __init__(self, val: int = None):
        self.val = val
        self.next = None

    def fill(self, collection: Iterable[int]) -> None:
        """Fill the linked list with elements from the collection."""
        for item in collection:
            self.append(item)

    def get_list(self) -> list:
        """Retrieve the values from the linked list as a Python list."""
        node = self
        lst = []
        while node:
            lst.append(node.val)
            node = node.next
        return lst

    def get_elem(self, val: int):
        node = self
        itr = 0
        while node.next and val - 1 >= itr:
            node = node.next
            itr += 1
        return node

    def append(self, val: int) -> None:
        """Add new value to the end of the linked list."""
        if self.val is None:
            self.val = val
            return

        node = self
        while node.next:
            node = node.next
        node.next = ListNode(val)
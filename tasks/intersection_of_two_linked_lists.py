# Link -> https://leetcode.com/problems/intersection-of-two-linked-lists/
# Author: Ilya Shvarev


from typing import Optional

from structures.LIST import ListNode



class Solution:

    @staticmethod
    def getIntersectionNode(head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        if not head1 or not head2:
            return None

        node1 = head1
        node2 = head2

        while node1 != node2:
            node1 = node1.next if node1 else head2
            node2 = node2.next if node2 else head1

        return node1


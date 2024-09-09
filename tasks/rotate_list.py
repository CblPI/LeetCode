# Link -> https://leetcode.com/problems/rotate-list
# Author: Ilya Shvarev

from structures.LIST import ListNode


class Solution:
    @staticmethod
    def rotateRight(head: ListNode, k: int) -> ListNode:

        if not head or not head.next or k == 0:
            return head

        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        k = k % length
        if k == 0:
            return head

        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        current.next = head

        return new_head
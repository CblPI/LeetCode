# Link -> https://leetcode.com/problems/add-two-numbers
# Author: Ilya Shvarev


from typing import Optional
from structures.LIST import ListNode


class Solution:
    @staticmethod
    def addTwoNumbers(lst1: Optional[ListNode], lst2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        carry = 0

        while lst1 or lst2 or carry:
            val1 = lst1.val if lst1 else 0
            val2 = lst2.val if lst2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if lst1:
                lst1 = lst1.next
            if lst2:
                lst2 = lst2.next

        return head.next
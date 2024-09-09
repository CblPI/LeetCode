# Link -> https://leetcode.com/problems/linked-list-cycle-ii/description/
# Author: Ilya Shvarev


from typing import Optional

from structures.LIST import ListNode


class Solution:
    @staticmethod
    def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        one = two = head

        while two and two.next:
            one = one.next
            two = two.next.next

            if one == two:
                break
        else:
            return None

        one = head
        while one != two:
            one = one.next
            two = two.next

        return one
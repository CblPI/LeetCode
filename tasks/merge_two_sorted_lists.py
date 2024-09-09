# Link -> https://leetcode.com/problems/merge-two-sorted-lists
# Author: Ilya Shvarev


from structures.LIST import ListNode


class Solution:

    @staticmethod
    def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:

        empty = ListNode()
        current = empty

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return empty.next



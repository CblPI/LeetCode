# Link -> https://leetcode.com/problems/palindrome-linked-list
# Author: Ilya Shvarev


from structures.LIST import ListNode


class Solution:
    @staticmethod
    def isPalindrome(head: ListNode) -> bool:
        if not head or not head.next:
            return True

        one = two = head
        while two and two.next:
            one = one.next
            two = two.next.next

        prev = None
        while one:
            next_node = one.next
            one.next = prev
            prev = one
            one = next_node

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True